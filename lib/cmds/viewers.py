from requests import get


def cmd(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/streams/{arg}"

    headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
    resp = get(url(channel["id"]), headers=headers).json()

    try:
        touser = args[0]
    except IndexError:
        touser = user["name"]

    try:
        viewers = resp["stream"]["viewers"]
    except TypeError:
        self.send_message(f"@{touser}, {channel['name'][1:]} is not live FeelsBadMan", channel["name"])
        return
    self.send_message(f"@{touser}, {viewers} Viewers are watching this stream currently.", channel["name"])
