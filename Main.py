import json

import irc.bot
from irc.bot import SingleServerIRCBot
from requests import get
import time
import logging as log
from lib.cmds import init, auto_msg
from lib.data import setup
from lib.cmds import utils
from threading import Thread
log.basicConfig(level=log.INFO, filename="lib/data/log.log")


def timestamp():
    return str(time.strftime("[%m/%d/%Y at %H:%M:%S]", time.localtime()))


class Bot(SingleServerIRCBot):
    def __init__(self):
        self.NAME = setup.startup()["bot_name"]
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = self.NAME.lower()
        self.BOTCHANNEL = f"#{self.USERNAME}"
        self.CLIENT_ID = setup.startup()["client_id"]
        self.TOKEN = setup.startup()["token"]
        self.SETUP = setup
        self.START = False
        uget = utils.Get(self.CLIENT_ID, self.TOKEN)
        self.get = uget.get

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
        resp = get(url, headers=headers).json()
        self.channel_id = resp["users"][0]["_id"]

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        log.info("")
        cxn.join(self.BOTCHANNEL)

        print(f"{timestamp()} [JOIN] {self.BOTCHANNEL}")
        log.info(f"{timestamp()} [JOIN] {self.BOTCHANNEL}")
        channels = setup.channels()
        for channel in channels:
            cxn.join(channel)
            print(f"{timestamp()} [JOIN] {channel}")
            log.info(f"{timestamp()} [JOIN] {channel}")
        log.info("")
        if self.START is False:
            t = Thread(target=hydrate, args=[self])
            t.start()
            self.START = True

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"], "mod": tags["mod"], "sub": tags["subscriber"]}
        channel = {'name': event.target, "id": tags["room-id"]}
        message = event.arguments[0]

        log.info(f"{timestamp()} [MESSAGE] in {channel['name']} from {user['name']}: {message}")

        init.process(self, user, message, channel, tags, cxn)
        auto_msg.automsg(self, message, user, channel)

    def send_message(self, message, channel):
        self.connection.privmsg(channel, message)

    # def usernotis(self, user, channel):
        # self.connection.send_items('USERNOTIS', str(channel), ':', str(user["name"]))


def settings(module):
    return setup.settings()[module] == "True"


def hydrate(self):
    file = open("lib/data/hydrate.json", "r+")
    data = json.load(file)
    next_ping = data["next_ping"]
    while True:
        time.sleep(5)
        if settings("hydrate"):
            file = open("lib/data/hydrate.json", "r+")
            data = json.load(file)
            if time.time() >= next_ping:
                channels = data["channels"]
                pings = data["pings"]
                for channel in channels:
                    resp = self.get(f"users?login={channel[1:]}")
                    resp = self.get(f"streams/{resp['users'][0]['_id']}")
                    if not resp['stream'] is None:
                        self.send_message("FeelsOkayMan Stay Hydrated Chat DinkDank " + " ".join(pings[channel]), channel)
                next_ping = time.time() + 1800
                data["next_ping"] = next_ping
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)


if __name__ == "__main__":
    bot = Bot()
    bot.start()
