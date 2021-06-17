
def cmd(self, user, channel, args):
    try:
        user1 = args[0].lower()
        try:
            channel1 = args[1].lower()
        except IndexError:
            channel1 = channel["name"].lower()
            channel1 = channel1[1:len(channel1)]
            user1 = args[0].lower()
    except IndexError:
        user1 = user["name"].lower()
        channel1 = channel["name"].lower()
        channel1 = channel1[1:len(channel1)]
    self.send_message(f"https://logs.ivr.fi/?channel={channel1}&username={user1}", channel["name"])
