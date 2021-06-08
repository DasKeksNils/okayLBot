import json


def startup():
    with open("lib/data/secrets.json") as file:
        return json.load(file)


def pingpong():
    with open("lib/data/pingpong.json") as file:
        return json.load(file)


def settings():
    with open("lib/data/settings.json") as file:
        return json.load(file)


def channels():
    with open("lib/data/channels.json") as file:
        return json.load(file)


def alias():
    with open("lib/data/alias.json") as file:
        return json.load(file)
