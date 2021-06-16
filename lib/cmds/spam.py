from requests import get


def spam_cmd(self, channel, args):
    try:
        num = args[0]
    except IndexError:
        self.send_message(f"MrDestructoid Not Enough Arguments! please add a number.", channel["name"])
        return
    try:
        num = int(num)
    except ValueError:
        self.send_message(f"MrDestructoid Wrong Argument! please add a number.", channel["name"])
        return

    if num > 50:
        self.send_message("MrDestructoid Cannot spam more than 50 FeelsBadMan", channel["name"])
        return

    msg = " ".join(args[1:])
    for i in range(num):
        self.send_message(f"{msg}", channel["name"])


def massping(self, channel, args):
    resp = get(f"https://tmi.twitch.tv/group/user/{channel['name'][1:]}/chatters").json()
    chatters = resp["chatters"]["moderators"] + resp["chatters"]["vips"] + resp["chatters"]["viewers"]

    text = " ".join(args)
    for i in chatters:
        self.send_message(f"@{i} {text}", channel["name"])
