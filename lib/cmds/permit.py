import json


def cmd(self, user, channel, args):
    try:
        op = args[0]
    except IndexError:
        self.send_message("FeelsDankMan Not Enough Arguments! avalible arguments: add, remove, list", channel["name"])
        return
    try:
        permit_user = args[1].lower()
    except IndexError:
        permit_user = None

    file = open("lib/data/permit.json", "r+")
    data = json.load(file)

    if op == "list":
        if data == []:
            data = None
        self.send_message(f"@{user['name']} permited users are: {', '.join(data)}", channel["name"])

    elif op == "add":
        if permit_user is None:
            self.send_message(f"FeelsDankMan Not Enough Arguments. please specify a user", channel["name"])
            return
        if permit_user in data:
            self.send_message("FeelsDankMan User already permited.", channel["name"])
            return

        data.append(permit_user)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)
        self.send_message(f"@{user['name']}, {permit_user} permited. ApuApproved", channel["name"])

    elif op in ("remove", "rem", "delte", "del"):
        if permit_user is None:
            self.send_message(f"FeelsDankMan Not Enough Arguments. please specify a user", channel["name"])
            return
        if permit_user not in data:
            self.send_message("FeelsDankMan User is not permited.", channel["name"])
            return

        data.remove(permit_user)

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)
        self.send_message(f"@{user['name']}, {permit_user} permit removed. ApuApproved", channel["name"])
    else:
        self.send_message("FeelsDankMan Argument Not Found", channel["name"])
