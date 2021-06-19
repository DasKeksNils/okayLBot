import time


def cp_remind(self, channel, op):
    if op == "brille":
        ping = time.time() + 300
        cp_action = "Brille"
    elif op == "fluchen":
        ping = time.time() + 600
        cp_action = "Fluchen"
    elif op == "hut":
        ping = time.time() + 1800
        cp_action = "Hut"
    elif op in ("hintergrund", "hg", "licht"):
        ping = time.time() + 1800
        cp_action = "Hintergrund"
    elif op == "test":
        ping = time.time() + 10
        cp_action = "test"
    else:
        self.send_message(f"FeelsDankMan {op} not Found.", channel["name"])
        return
    self.send_message("Reminder set ApuApproved", channel["name"])
    while True:
        if time.time() >= ping:
            self.send_message(f"WEEWOO @me_kc {cp_action} rum WEEWOO", channel["name"])
            return
        time.sleep(5)
