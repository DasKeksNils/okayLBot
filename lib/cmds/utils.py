import json
import requests


def is_owner(self, user, channel):
    return user["id"] == channel["id"] or self.channel_id == user["id"] or is_permited(self, user)


def is_mod(self, user, channel):
    return user["mod"] == "1" or user["id"] == channel["id"] or self.channel_id == user["id"] or is_permited(self, user)


def is_sub(self, user, channel):
    return user["sub"] == "1" or user["mod"] == "1" or user["id"] == channel["id"] or is_permited(self, user)


def is_botchannel(self, channel):
    return self.BOTCHANNEL == channel["name"]


def is_bot_owner(self, user):
    return self.channel_id == user["id"]


def is_permited(self, user):
    file = open("lib/data/permit.json")
    data = json.load(file)
    return user["name"].lower() in data or user["id"] == self.channel_id


def is_admin(self, user):
    file = open("lib/data/admin.json")
    data = json.load(file)
    print(data)
    return user["name"].lower() in data or user["id"] == self.channel_id


class Get(object):
    def __init__(self, client_id, token):
        self.headers = {"Client-ID": client_id, "Accept": "application/vnd.twitchtv.v5+json",
                   "Authorization": f"OAuth {token}", "Content-Type": "application/json"}

    def get(self, ob):
        return requests.get(f"https://api.twitch.tv/kraken/{ob}", headers=self.headers).json()
