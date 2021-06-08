import json
import random


def cmd(self, channel, args):
    try:
        op = args[0].lower()
    except IndexError:
        self.send_message("MrDestructoid Not Enough Arguments! avalible arguments: wahrheit; plicht, drunk",
                          channel["name"])
        return

    file = open("lib/data/pyjama.json", "r+")
    data = json.load(file)
    try:
        liste = data[op]
    except KeyError:
        self.send_message("MrDestructoid Wrong Argument! avalible arguments: wahrheit; plicht; drunk",
                          channel["name"])
        return
    try:
        question = random.choice(liste)
    except IndexError:
        self.send_message(f"MrDestructoid No {op} questions avalible FeelsBadMan", channel["name"])
        return

    self.send_message(f"MrDestructoid Frage für {op} ist: {question}", channel["name"])
    liste.remove(question)
    data[op] = liste
    file.seek(0)
    file.truncate()
    json.dump(data, file, indent=4)
