import json


def module_cmd(self, user, channel, args):
    modules = ["me_kc", "timeout", "pingpong", "joy", "cookies", "hydrate"]
    try:
        module = args[0]
    except IndexError:
        module_list = ", ".join(modules)
        self.send_message(f"@{user['name']} module not found! avalible modules: {module_list}", channel["name"])
        return

    if module == "list":
        module_list = ", ".join(modules)
        self.send_message(f"MrDestructoid module not found! avalible modules: {module_list}", channel["name"])
        return

    if module.lower() not in modules:
        module_list = ", ".join(modules)
        self.send_message(f"MrDestructoid Avalible modules: {module_list}", channel["name"])
        return

    file = open("lib/data/settings.json", "r+")
    data = json.load(file)

    try:
        mod = data[module.lower()]
    except KeyError:
        return

    if mod == "True":
        mod = "False"
        data[module.lower()] = mod
        self.send_message(f"MrDestructoid Module {module} now set to off.", channel["name"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)
        return

    if mod == "False":
        mod = "True"
        data[module.lower()] = mod
        self.send_message(f"MrDestructoid Module {module} now set to on.", channel["name"])
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)
        return
