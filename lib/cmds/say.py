
def cmd(self, channel, args):
    channel_ = args[0]
    if channel_[0:1] == "#":
        channel_ = channel_[1:]
    self.send_message(" ".join(args[1:]), f"#{channel_}")
