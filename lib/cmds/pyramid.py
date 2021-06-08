
def cmd(self, channel, args):
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

    if num > 30:
        self.send_message("MrDestructoid Cannot build a pyramid higher than 30 FeelsBadMan", channel["name"])
        return

    msg = " ".join(args[1:])
    msg = msg + " "

    y = 0
    while num != y:
        text = msg * y
        if not len(text) >= 500:
            self.send_message(text, channel["name"])

        y = y + 1

    while y >= 0:
        text = msg * y
        if not len(text) >= 500:
            self.send_message(text, channel["name"])
        y = y - 1
