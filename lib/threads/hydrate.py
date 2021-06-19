import json
import time
from lib.data import setup


def settings(module):
    return setup.settings()[module] == "True"


def hydrate(self):
    file = open("lib/data/hydrate.json", "r+")
    data = json.load(file)
    next_ping = data["next_ping"]
    while True:
        time.sleep(5)
        if settings("hydrate"):
            file = open("lib/data/hydrate.json", "r+")
            data = json.load(file)
            if time.time() >= next_ping:
                channels = data["channels"]
                pings = data["pings"]
                for channel in channels:
                    resp = self.get(f"users?login={channel[1:]}")
                    resp = self.get(f"streams/{resp['users'][0]['_id']}")
                    if not resp['stream'] is None:
                        self.send_message("FeelsOkayMan Stay Hydrated Chat DinkDank " + " ".join(pings[channel]), channel)
                next_ping = time.time() + 1800
                data["next_ping"] = next_ping
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
