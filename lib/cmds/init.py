import json
from requests import get, put, post
import time

from lib.data import setup
from lib.cmds import channel_cmd
from lib.cmds import module
from lib.cmds import utils
from lib.cmds import followage
from lib.cmds import alias
from lib.cmds import spam
from lib.cmds import permit
from lib.cmds import pyramid
from lib.cmds import me
from lib.cmds import game
from lib.cmds import title
from lib.cmds import onlyfans
from lib.cmds import set
from lib.cmds import viewers
from lib.cmds import cock
from lib.cmds import user_cmds
from lib.cmds import hydrate
from lib.cmds import say
from lib.cmds import logs
from lib.cmds import channelpoints

PREFIX = setup.startup()["PREFIX"]


class Cmd(object):
    def __init__(self, callables, func, cooldown=0):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time.time()


def test(self, user, channel):
    # print(self.usernotis(user, channel))
    self.send_message("test_wsiorjkaekomhetrh", channel["name"])


def settings(module):
    return setup.settings()[module] == "True"


cmds = {
    Cmd(["test"], test, cooldown=15),
}


def process(self, user, message, channel, tags, cxn):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        print(cmd)
        args = message.split(" ")[1:]
        print(args)
        perform(self, cxn, tags, user, channel, cmd, *args)
    else:
        return


def perform(self, cxn, tags, user, channel, cmd, *args):
    cmd = cmd.lower()
    ALIAS = setup.alias()

    if cmd == "ping" or cmd in ALIAS["ping"]:
        self.send_message("Pong FeelsDankMan 🏓 ppHop 🏓 💻  ", channel["name"])

    if cmd == "join" or cmd in ALIAS["join"]:
        if utils.is_botchannel(self, channel):
            if utils.is_mod(self, user, channel):
                channel_cmd.join(self, cxn, channel, args)

    if cmd == "part" or cmd in ALIAS["part"]:
        if utils.is_botchannel(self, channel):
            if utils.is_mod(self, user, channel):
                channel_cmd.part(self, cxn, channel, args)

    if cmd == "channels" or cmd in ALIAS["channels"]:
        if utils.is_botchannel(self, channel):
            channel_cmd.ch_list(self, channel)

    if cmd == "commands" or cmd in ALIAS["commands"]:
        self.send_message(f"@{user['name']} list of all commands: https://github.com/DasKeksNils/okayLBot#commands", channel["name"])

    if cmd == "github" or cmd in ALIAS["github"]:
        self.send_message("Github repository 👉 https://github.com/DasKeksNils/okayLBOt", channel["name"])

    if cmd == "module" or cmd in ALIAS["module"]:
        if utils.is_permited(self, user):
            module.module_cmd(self, user, channel, args)

    if cmd == "followage" or cmd in ALIAS["followage"]:
        followage.cmd(self, user, channel, args)

    if cmd == "alias" or cmd in ALIAS["alias"]:
        if utils.is_botchannel(self, channel):
            if utils.is_mod(self, user, channel):
                alias.cmd(self, user, channel, args)

    if cmd == "spam" or cmd in ALIAS["spam"]:
        if utils.is_mod(self, user, channel):
            spam.spam_cmd(self, channel, args)

    if cmd == "permit" or cmd in ALIAS["permit"]:
        if utils.is_admin(self, user):
            permit.cmd(self, user, channel, args)

    if cmd == "pyramid" or cmd in ALIAS["pyramid"]:
        if utils.is_mod(self, user, channel):
            pyramid.cmd(self, channel, args)

    if cmd == "game" or cmd in ALIAS["game"]:
        game.cmd(self, user, channel, args)

    if cmd == "title" or cmd in ALIAS["title"]:
        title.cmd(self, user, channel, args)

    if cmd == "me" or cmd in ALIAS["me"]:
        if utils.is_permited(self, user):
            me.cmd(self, channel, args)

    if cmd == "onlyfans" or cmd in ALIAS["onlyfans"]:
        onlyfans.cmd(self, user, channel, args)

    if cmd == "settitle" or cmd in ALIAS["settitle"]:
        if utils.is_mod(self, user, channel):
            set.title(self, user, channel, args)

    if cmd == "seteditgame" or cmd in ALIAS["seteditgame"]:
        if utils.is_permited(self, user):
            set.editgame(self, user, channel, args)

    if cmd == "setgame" or cmd in ALIAS["setgame"]:
        if utils.is_mod(self, user, channel):
            set.game(self, user, channel, args)

    if cmd == "cock" or cmd in ALIAS["cock"]:
        cock.cmd(self, user, channel, args)

    if cmd == "viewer" or cmd in ALIAS["viewer"]:
        viewers.cmd(self, user, channel, args)

    if cmd == "vanish" or cmd in ALIAS["vanish"]:
        user_cmds.vanish(self, user, channel)

    if cmd == "color" or cmd in ALIAS["color"]:
        user_cmds.color(self, user, channel, tags)

    if cmd == "ispartner" or cmd in ALIAS["ispartner"]:
        user_cmds.partner(self, user, channel, args)

    if cmd == "massping" or cmd in ALIAS["massping"]:
        if utils.is_owner(self, user, channel):
            spam.massping(self, channel, args)

    if cmd == "kock" and channel["id"] == "439341700":
        self.send_message(f"@{user['name']} the Kock is 160cm long HandsUp", channel["name"])

    if cmd == "say" or cmd in ALIAS["say"]:
        if utils.is_permited(self, user):
            say.cmd(self, args)

    if cmd == "hydrate" or cmd in ALIAS["hydrate"]:
        hydrate.cmd(self, user, channel, args)

    if cmd == "logs" or cmd in ALIAS["logs"]:
        logs.cmd(self, user, channel, args)

    if cmd == "google" or cmd in ALIAS["google"]:
        self.send_message(f"{user['name']}, https://www.google.com/search?q={'+'.join(args)}", channel["name"])

    if cmd == "subage" or cmd in ALIAS["subage"]:
        try:
            user1 = args[0]
            try:
                channel1 = args[1].lower()
            except IndexError:
                channel1 = args[0]
                user1 = user["name"].lower()
        except IndexError:
            user1 = user["name"].lower()
            channel1 = channel["name"]
            channel1 = channel1[1:].lower()

        resp = get(f"https://api.ivr.fi/twitch/subage/{user1}/{channel1}").json()
        print(resp)

    if cmd == "channelpoints" or cmd in ALIAS["channelpoints"]:
        if utils.is_mod(self, user, channel):
            channelpoints.cmd(self, user, channel, args)

    for command in cmds:
        if cmd in command.callables:
            if time.time() >= command.next_use:
                command.func(self, user, channel)
                command.next_use = time.time() + command.cooldown
            else:
                self.send_message(f"Cooldown still in effect. Try again in {command.next_use-time.time():,.0f} seconds.", channel["name"])

            return
