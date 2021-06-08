from requests import get
import random


def color(self, user, channel, tags):
    self.send_message(f"@{user['name']} your color is {tags['color']}", channel["name"])


def vanish(self, user, channel):
    self.send_message(f"/timeout {user['name']} 1s vanish", channel["name"])


def partner(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/{arg}"

    headers = {"Client-ID": self.CLIENT_ID, "Authorization": f"OAuth {self.SETUP.startup()['token']}",
               "Accept": "application/vnd.twitchtv.v5+json"}
    try:
        touser = args[0].lower()
    except IndexError:
        touser = user['name'].lower()

    resp = get(url(f"users?login={touser.lower()}"), headers=headers).json()

    touser_id = resp["users"][0]["_id"]

    resp = get(url(f"channels/{touser_id}"), headers=headers).json()

    self.send_message(f"User: {resp['display_name']} | Partner: {resp['partner']}", channel["name"])
