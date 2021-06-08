import json
import time
import logging as log

log.basicConfig(level=log.INFO, filename="lib/data/log.log")


def timestamp():
    return str(time.strftime("[%m/%d/%Y at %H:%M:%S]", time.localtime()))


def join(self, cxn, channel, args):
    try:
        join_channel = args[0].lower()
    except IndexError:
        self.send_message("MrDestructoid Not Enough Arguments FeelsDankMan", channel["name"])
        return
    if not join_channel[0:1] == "#":
        join_channel = f"#{join_channel}"

    file = open("lib/data/channels.json", "r+")
    data = json.load(file)

    channels = data
    if join_channel in channels or join_channel == self.BOTCHANNEL:
        self.send_message(f"MrDestructoid bot is already in {join_channel} FeelsDankMan", channel['name'])
    else:
        cxn.join(join_channel)
        self.send_message(f"MrDestructoid successfully joined {join_channel} ApuApproved", channel['name'])

        print(f"{timestamp()} [JOIN] {join_channel}")
        log.info(f"{timestamp()} [JOIN] {join_channel}")

        channels.append(join_channel)
        data = channels
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)


def part(self, cxn, channel, args):
    try:
        part_channel = args[0].lower()
    except IndexError:
        self.send_message("MrDestructoid Not Enough Arguments FeelsDankMan", channel["name"])
        return
    if not part_channel[0:1] == "#":
        part_channel = f"#{part_channel}"
    if part_channel == self.BOTCHANNEL:
        self.send_message("MrDestructoid cannot leave own channel.", channel['name'])
        return

    file = open("lib/data/channels.json", "r+")
    data = json.load(file)
    channels = data
    try:
        channels.remove(part_channel)
    except ValueError:
        self.send_message(f"MrDestructoid bot is not in {part_channel} FeelsDankMan", channel['name'])
        return

    cxn.part(part_channel)
    self.send_message(f"MrDestructoid successfully leaved {part_channel} ApuApproved", channel['name'])

    print(f"{timestamp()} [PART] {part_channel}")
    log.info(f"{timestamp()} [PART] {part_channel}")

    data = channels
    file.seek(0)
    file.truncate()
    json.dump(data, file, indent=4)


def ch_list(self, channel):
    file = open("lib/data/channels.json", "r+")
    data = json.load(file)
    channels = ", ".join(data)

    self.send_message(f"MrDestructoid I'm active in: {channels}", channel['name'])
