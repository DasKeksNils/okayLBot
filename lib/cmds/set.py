from requests import get, put


def title(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/{arg}"

    title_ = '{"channel": {"status": \"' + " ".join(args) + '\"}}'

    headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json",
               "Authorization": f"OAuth {self.TOKEN}", "Content-Type": "application/json"}

    resp = put(url(f"channels/{channel['id']}"), headers=headers, data=title_).json()

    if resp == {'error': 'Forbidden', 'status': 403, 'message': 'Fail to auth.'}:
        self.send_message("MrDestructoid I'm not authorized to do that.", channel["name"])
        return

    self.send_message(f"@{user['name']} changed the title to: {resp['status']}", channel["name"])


def editgame(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/{arg}"

    game_ = '{"channel": {"game": \"' + " ".join(args) + '\"}}'

    headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json",
               "Authorization": f"OAuth {self.TOKEN}", "Content-Type": "application/json"}

    resp = put(url(f"channels/{channel['id']}"), headers=headers, data=game_).json()

    if resp == {'error': 'Forbidden', 'status': 403, 'message': 'Fail to auth.'}:
        self.send_message("MrDestructoid I'm not authorized to do that.", channel["name"])
        return

    self.send_message(f"@{user['name']} changed the game to: {resp['game']}", channel["name"])


def game(self, user, channel, args):
    def url(arg):
        return f"https://api.twitch.tv/kraken/{arg}"

    headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json",
               "Authorization": f"OAuth {self.TOKEN}", "Content-Type": "application/json"}

    game_api = get(url(f"search/games?query={' '.join(args)}"), headers=headers).json()

    game_ = '{"channel": {"game": \"' + game_api['games'][0]['name'] + '\"}}'

    resp = put(url(f"channels/{channel['id']}"), headers=headers, data=game_).json()

    if resp == {'error': 'Forbidden', 'status': 403, 'message': 'Fail to auth.'}:
        self.send_message("MrDestructoid I'm not authorized to do that.", channel["name"])
        return

    self.send_message(f"@{user['name']} changed the game to: {resp['game']}", channel["name"])
