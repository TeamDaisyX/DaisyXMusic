<h1 align="center">DAISYX MUSIC V6.0 🎵</h1>

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [PYTGCALLS](https://github.com/pytgcalls/pytgcalls)
### Available on telegram as [@DaisyXbot](https://t.me/daisyxbot)

<p align="center">
  <img src="https://telegra.ph/file/dd04b1968f1bc1169d162.jpg">
</p>

<h2> Features 🔥 </h2>

- Thumbnail Support
- Playlist Support
- Current playback support
- Showing track names when skipping
- Zero downtime, Fully Stable
- Youtube playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play

## 🚀 Deployment

### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Get pyrogram (p)  `SESSION` from here:

[![Run on Repl.it](https://repl.it/badge/github/Makoto-XD/Session-Generator)](https://replit.com/@Makoto-XD/Session-Generator)

### ⚔ Self-hosting
```sh
# First Upgrade Your Terminal
$ sudo su (if terminal not have root access)
$ cd (if terminal not have root access)
$ apt update && apt upgrade -y
$ apt install python ffmpeg -y
$ curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash -
$ apt install nodejs -y
$ pip3 install -U pip
$ npm i -g npm
# Now Do Git Clone
$ git clone https://github.com/TeamDaisyX/DaisyXmusic
$ cd DaisyXMusic
# Upgrade sources
# Install All Requirements 
$ pip3 install -U -r requirements.txt
# Now Edit example.env and enter your creds
$ cp example.env .env
# Now start the Bot
$ python3 -m DaisyXMusic
```

### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/play <reply to audio>` - play replied file
- `/ytplay <song name>`: Directly play song via Youtube Music
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/video <song name>` - download videos you want quickly

#### Admins only.
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/mute` - mute song play
- `/unmute` - unmute song play
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/admincache` - Refresh admin list
- `/musicplayer [on/off]` - Enable/Disable Music Player

### Commands for Channel Music Play 🛠
For linked group admins only:
- `/cplay <song name>` - play song you requested
- `/cplay <reply to link>` - play replied youtube link
- `/cplay <reply to audio>` - play replied file
- `/cplaylist` - Show now playing list
- `/cccurrent` - Show now playing
- `/cplayer` - open music player settings panel
- `/cpause` - pause song play
- `/cresume` - resume song play
- `/cskip` - play next song
- `/cend` - stop music play
- `/cmute` - mute song play
- `/cunmute` - unmute song play
- `/userbotjoinchannel` - invite assistant to your chat
* channel is also can be used instead of c

If you donlt like to play in linked channel:
 1. Get your channel ID.
 2. Rename your group to: Channel Music: your_channel_id
 3. Add @DaisyXBot as Channel admin with full perms
 4. add helper to channel
 5. Simply send commands in your group.

### Commands for Sudo Users ⚔️
- `/userbotleaveall` - remove assistant from all chats
- `/gcast <reply to message>` - globally brodcast replied message to all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
+ Sudo Users can execute any command in any groups


## Special Credits
- [Dan](https://github.com/delivrance) For [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Laky-64](https://github.com/Laky-64) For [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

### Inspiration
- [Callsmusic](http://github.com/callsmusic/callsmusic)
- [tgvc-userbot](https://github.com/callsmusic/tgvc-userbot)

#### Contributors
- [InukaAsith](https://github.com/InukaAsith): Dev / Owner
- [lucifeermorningstar](https://github.com/lucifeermorningstar): Dev / Owner
- [Hellboy-OP](https://github.com/hellboy-op)
- [Roj Serbest](http://github.com/rojserbest): Developer of callsmusic 
- [DeshadeethThisarana](https://github.com/deshadeeth-thisarana): Dev
- [Wrench](https://github.com/EverythingSuckz/): Dev
- [Bemro](https://github.com/bemroofficial): Dev
- [QueenArzoo](https://github.com/QueenArzoo): Dev
- [Anjana-Ma](https://github.com/Anjana-Ma): Dev
- [ImJanindu](https://github.com/ImJanindu): Dev
- [azimazizov9150](https://github.com/azimazizov9150): Contributor


## Copyright & License 👮

 - Copyright (C) 2020-present by [TeamDaisyX](github.com/teamdaisyx) ❤️️
 - Licensed under the terms of the [MIT License](https://github.com/TeamDaisyX/DaisyXMusic/blob/master/LICENSE)
    
DaisyXMusic is Free Software: You can use, study share and improve it at your will. Specifically you can redistribute and/or modify it under the terms of the MIT License as published by the Free Software Foundation.    
## Made with ♥️ by [TeamDaisyX](https://github.com/TeamDaisyX)
