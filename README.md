# okayLBot

[![CodeFactor](https://www.codefactor.io/repository/github/daskeksnils/okayLBot/badge/main)](https://www.codefactor.io/repository/github/daskeksnils/okayLBot/overview/main)
![MIT LICENS](https://camo.githubusercontent.com/addaf52c6b92a0a6766d931fa5fd0344b569429efeacb8c128d170527d2e221c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f50686f656e697847616d65732d50686f656e69782f5363726970744465636b)

## Info

This is a Twitch Bot from DasKeksNils. If you want this bot in your channel, please write a twitch dm to @DasKeksNils okayL

---
## Stay Hydrated Bot

This module sends a "Stay Hydrated" message with cutsom pings to all added channels.
You can add a channel as mod from the channel (view commands).
This message will sended every 30min to all onchats.

---
## Commands:

### Permission levels:

 0 -All Users

 0,5 - All Users; cmd only avalible in #okayLBot

 1 - Mod in the channel

 2 - Mod in channel #okayLBot

 3 - Broadcaster

 4 - Permited User

 5 - Bot Owner - includes admins

------

###Prefix: *

|COMMAND   |REQUIRED ARGUMENTS   | OPTIONAL ARGUMENTS   | PERMISSION LEVEL   |COOLDOWN   | NOTES |
|---|---|---|---|---| --- |
|alias  |add/remove/list   |command; alias(es)   | 0  | /  | / |
|ban_bots | / | / | 1 | / | experimental; bans ip grabber |
|channelpoints | action | / | 1 | / | only in #me_kc
|channels   |/   |/   |0,5   |/   | / |
|cock | / | user | 0  | / | / |
|color | / | / | 0 | / | / |
|commands   |/   |user   |0   |/   | / |
|coinflip | / | / | 0 | / | / |
|followage  |/   |user or channel, user   | 0   |/   | testing |
|game   |/   |user   |0   |/   | / |
|github | / | /     | 0   | /  | / |
|google | text | / | 0 | / | / |
|hydrate | pingme/remping | / | 0 | / | channel must be added |
|hydrate | add-/remmychannel | / | 1 | / | / |
|ispartner | / | channel | 0 | / | / |
|join   |channel   |/   |2   |/   | / |
|kock | / | user | 0 | / | only in #me_kc |
|logs |user | channel | 0 | / | logs from logs.ivr.fi |
|massping | text | / | 3 | / | / |
|me   |wahrheit/pflicht/drunk   |/   |4   |/   | only in #me_kc |
|module   |module   |/   |4   |/   | / |
|onlyfans   |/   |user   |0   |/   | / |
|part   |channel   |/   |2   |/   | / |
|permit   |add/remove/list, user   |/   |5   |/   | / |
|ping   |/   |/   |1   |/   | / |
|pyramid   |number, text   |/   |1   |/   | / |
|say | channel, text | / | 4 | / | / |
|seteditgame | game | / | 4 | / | bot needs editor; sets raw input|
|setgame | game | / | 1 | / | bot needs editor|
|settitle | title | / | 1 | / | bot needs editor|
|spam   |number, text   |/   |1   |/   | / |
|subage | / | user/ channel, user | 5 | / | testing |
|stalk | user | channel | 0 | / | is in viewerlist |
|test |/ | / | 4 | 15 | testing cooldown |
|title   |/   |user   |0   |/   | / |
|uptime | / | / | 0 | / | uptime from bot |
|vanish| / | / | 0 | / | / |
|viewer | / | user | 0 | / | shows viewercount |

