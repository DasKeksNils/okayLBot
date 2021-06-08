import random


def cmd(self, user, channel, args):
    try:
        touser = args[0]
    except IndexError:
        touser = user["name"]

    self.send_message(f"{touser} \'s cock is {random.choice(range(0, 30))}cm long HandsUp", channel["name"])
