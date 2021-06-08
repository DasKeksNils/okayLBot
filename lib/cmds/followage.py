from requests import get
import time
from datetime import datetime


def cmd(self, user, channel, args):

    def url(arg):
        return f"https://api.twitch.tv/kraken/{arg}"

    headers = {"Client-ID": self.CLIENT_ID, "Authorization": f"OAuth {self.SETUP.startup()['token']}",
               "Accept": "application/vnd.twitchtv.v5+json"}

    try:
        user1 = args[0]
        try:
            channel1 = args[1]
        except IndexError:
            channel1 = args[0]
            user1 = user["name"]
    except IndexError:
        user1 = user["name"]
        channel1 = channel["name"]
        channel1 = channel1[1:len(channel1)]

    if user1.lower() == channel1.lower():
        self.send_message(
            f"@{user['name']}, you cannot follow yourself FeelsBadMan", channel["name"])
        return
    resp = get(url(f"users?login={user1.lower()},{channel1.lower()}"), headers=headers).json()

    if resp["_total"] <= 1:
        self.send_message("MrDestructoid Not Found", channel["name"])
        return

    sub_user_id = resp["users"][0]["_id"]
    sub_channel_id = resp["users"][1]["_id"]

    fa = get(url(f"users/{sub_user_id}/follows/channels/{sub_channel_id}"), headers=headers).json()
    print(fa)
    #2021-02-12T14:44:03Z

    FMT = "%Y-%m-%dT%H:%M:%SZ"
    gmt = time.strftime(FMT, time.gmtime())
    print(gmt)

    follow_time = datetime.strptime(fa['created_at'], FMT)
    now_time = datetime.strptime(gmt, FMT)
    tdelta_month = (follow_time.year - now_time.year) * 12 + (follow_time.month - now_time.year)
    print(tdelta_month)

    try:
        if fa['message'] == "Follow not found":
            self.send_message(
                f"@{user['name']}, {resp['users'][0]['display_name']} is not following {resp['users'][1]['display_name']} FeelsBadMan",
                channel['name'])
            return
    except KeyError:
        self.send_message(
            f"@{user['name']}, {resp['users'][0]['display_name']} is followig {resp['users'][1]['display_name']} since {fa['created_at']}",
            channel['name'])
