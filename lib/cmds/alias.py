import json


def cmd(self, user, channel, args):
    try:
        op = args[0].lower()

    except IndexError:
        self.send_message("MrDestructoid Not Enough Arguments! avlible arugments: list, add, remove", channel["name"])
        return
    try:
        cmd_alias = args[1].lower()
    except IndexError:
        self.send_message("MrDestructoid Not Enough Arguments! You have to specify a command!", channel["name"])
        return

    aliases = args[2:]
    if aliases == ():
        aliases = None

    file = open("lib/data/alias.json", "r+")
    data = json.load(file)

    if op == "list":
        try:
            output = ", ".join(data[cmd_alias])
            if output == "":
                output = "{no alias}"
            self.send_message(f"@{user['name']} Command aliases for {cmd_alias} are: {output}", channel["name"])
        except KeyError:
            self.send_message(f"MrDestructoid Command {cmd_alias} not Found!", channel["name"])
            return

    if op == "add":
        try:
            output = data[cmd_alias]
        except KeyError:
            self.send_message(f"MrDestructoid Command {cmd_alias} not Found!", channel["name"])
            return
        if aliases is None:
            self.send_message("MrDestructoid Not Enough Arguments! No Aliases!", channel["name"])
            return

        for i in aliases:
            output.append(i)

        data[cmd_alias] = output
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)

        self.send_message(f"@{user['name']} added alias(es) {', '.join(aliases)} to command {cmd_alias}.",
                          channel["name"])

    if op in ("rem", "remove", "del", "delte"):
        try:
            output = data[cmd_alias]
        except KeyError:
            self.send_message(f"MrDestructoid Command {cmd_alias} not Found!", channel["name"])
            return
        if aliases is None:
            self.send_message("MrDestructoid Not Enough Arguments! No Aliases!", channel["name"])
            return
        try:
            for i in aliases:
                output.remove(i)
        except ValueError:
            self.send_message(f"MrDestructoid {' '.join(aliases)} is no alias from {cmd_alias}", channel["name"])
            return

        data[cmd_alias] = output
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)

        self.send_message(f"@{user['name']} removed alias(es) {', '.join(aliases)} from command {cmd_alias}.",
                          channel["name"])
