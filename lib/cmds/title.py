from requests import get


def cmd(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/channels/{arg}"

    headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
    resp = get(url(channel["id"]), headers=headers).json()
    try:
        touser = args[0]
    except IndexError:
        touser = user["name"]

    self.send_message(f"@{touser}, the title of {resp['display_name']} is: {resp['status']}", channel["name"])
