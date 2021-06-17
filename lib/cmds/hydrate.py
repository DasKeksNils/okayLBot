import json
from lib.cmds import utils


def cmd(self, user, channel, args):
    try:
        op = args[0].lower()
    except IndexError:
        self.send_message("FeelsDankMan Not Enough Arguments.", channel["name"])
        return

    file = open("lib/data/hydrate.json", "r+")
    data = json.load(file)
    channels = data["channels"]
    pings = data["pings"]

    if op == "addmychannel":
        if utils.is_mod(self, user, channel):

            if not channel["name"] in channels:
                channels.append(channel["name"])
                pings[channel["name"]] = []
                data["pings"] = pings
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                self.send_message("You have added your channel to the Stay Hydrated Bot ApuApproved", channel["name"])
            else:
                self.send_message("FeelsDankMan Channel already added.", channel["name"])

    if op == "removemychannel":
        if utils.is_mod(self, user, channel):
            if channel["name"] in channels:
                channels.remove(channel["name"])
                data["channels"] = channels
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                self.send_message("You have removed your channel from the Stay Hydrated Bot FeelsBadMan",
                                  channel["name"])
            else:
                self.send_message("FeelsDankMan Channel not added.")

    if op in ("addping", "ping", "pingme"):
        if channel["name"] in channels:
            ping_channel = pings[channel["name"]]
            if not user["name"].lower() in ping_channel:
                ping_channel.append(user["name"].lower())
                data["pings"][channel["name"]] = ping_channel
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                self.send_message(f"@{user['name']} successfully added ping in this channel ApuApproved",
                                  channel["name"])
            else:
                self.send_message(f"@{user['name']} you have already a ping in this channel FeelsDankMan",
                                  channel["name"])
        else:
            self.send_message("Channel has the Stay Hydrated Bot not activated FeelsBadMan", channel["name"])

    if op in ("removeping", "delping", "remping", "deleteping"):
        if channel["name"] in channels:
            ping_channel = pings[channel["name"]]
            if user["name"].lower() in ping_channel:
                if user["id"] == "489167137" and channel["id"] == "439341700":
                    self.send_message("Yo moritz einfach nein :)", channel["name"])
                    return
                ping_channel.remove(user["name"].lower())
                data["pings"][channel["name"]] = ping_channel
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
                self.send_message(f"@{user['name']} successfully removed ping in this channel ApuApproved", channel["name"])
            else:
                self.send_message(f"@{user['name']} you don't have a ping in this channel FeelsDankMan", channel["name"])
        else:
            self.send_message("Channel has the Stay Hydrated Bot not activated FeelsBadMan", channel["name"])
