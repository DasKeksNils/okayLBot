from lib.threads.channelpoints import cp_remind
from threading import Thread


def cmd(self, user, channel, args):
    if channel["id"] == "439341700" or channel["id"] == self.channel_id:
        try:
            op = args[0].lower()
        except IndexError:
            self.send_message(f"@{user['name']} Not Enough Arguments FeelsDankMan", channel["name"])
            return
        t = Thread(target=cp_remind, args=[self, channel, op])
        t.start()
