import random
from lib.data import setup


def settings(module):
    return setup.settings()[module] == "True"


def automsg(self, message, user, channel):

    if user['name'].lower() == self.USERNAME:
        return

    if "Such das Herz und klick drauf 4Heed" in message and settings("me_kc"):
        self.send_message("4Heed", channel["name"])

    if "Falls ihr mir einen Tip geben wollt haHAA" in message and settings("me_kc"):
        self.send_message("haHAA", channel["name"])

    if "played GG" in message and settings("me_kc"):
        self.send_message("GG!", channel["name"])

    if "played Rip" in message and settings("me_kc"):
        self.send_message("FeelsRainMan RIP 🕯", channel["name"])

    if "Twitch Prime ist Kostenlos POGGERS" in message and settings("me_kc"):
        self.send_message("!prime POGGERS", channel["name"])

    if "played DICKS for" in message and settings("me_kc"):
        self.send_message("DICKS", channel["name"])

    if "played orgasm for" in message and settings("me_kc"):
        self.send_message("Kreygasm", channel["name"])

    if "played Harder Daddy" in message and settings("me_kc"):
        self.send_message("Kreygasm", channel["name"])

    if "played Vodka for" in message and settings("me_kc"):
        self.send_message("pepeJAM gib mir den Wodka anuschka FeelsBlyatMan und dann lass mich sein FeelsBlyatMan der Wodka ist freundlich FeelsBlyatMan doch du bist gemein pepeJAM", channel["name"])

    if "https://stats.StreamElements.com/c" in message and settings("me_kc"):
        self.send_message("PogChamp", channel["name"])

    if "Subs Jammies" in message and settings("me_kc"):
        self.send_message("Jammies", channel["name"])

    if "played Awkward Fart for" in message and settings("me_kc"):
        self.send_message("DansGame", channel["name"])

    if "played It was at this moment that he knew..." in message and settings("me_kc"):
        self.send_message("mekcFail", channel["name"])

    if "Bits gespendet" in message and settings("me_kc"):
        self.send_message("PogChamp", channel["name"])

    if "😂" in message and settings("joy"):
        self.send_message(f"@{user['name']} revedJoy 🔫", channel["name"])

    if "🏓 ppOverHeat 🏓" in message and settings("pingpong"):
        self.send_message(f"{random.choice(setup.pingpong()['emote1'])} 🏓 ppOverHeat 🏓 {random.choice(setup.pingpong()['emote2'])}", channel["name"])

    if "DansGame FBBlock Jammies" in message and settings("timeout"):
        self.send_message(f"/timeout {user['name']} 1s Jammies rise!", channel["name"])
