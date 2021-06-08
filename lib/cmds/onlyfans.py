
def cmd(self, user, channel, args):
    touser = " ".join(args)
    if touser == "":
        touser = user["name"]

    self.send_message(f"peepoRiot {touser} soll onlyfans machen!", channel["name"])
