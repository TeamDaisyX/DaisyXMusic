<h1 align="centre">DAISYXMUSIC V5.0 🎵</h1>

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [MARSHALX TGCALLS](https://github.com/MarshalX/tgcalls)
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
- Deezer,Youtube & Saavn playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play

## 🚀 Deployment

### 💜 Heroku/Railway

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TeamDaisyX/DaisyXMusic)
[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/TeamDaisyX/DaisyXMusic&envs=SESSION_NAME,BOT_TOKEN,BOT_USERNAME,BOT_NAME,SUPPORT_GROUP,PROJECT_NAME,ARQ_API_KEY,ASSISTANT_NAME,BG_IMAGE,UPDATES_CHANNEL,API_ID,API_HASH,SUDO_USERS,DURATION_LIMIT)

Get pyrogram (p)  `SESSION` from here:

[![Run on Repl.it](https://repl.it/badge/github/ChankitSaini/GenerateStringSession)](https://replit.com/@ChankitSaini/GenerateStringSession)

### ⚔ Self-hosting (For Devs) 
```sh
# Install Git First (apt-get install git)
$ git clone https://github.com/TeamDaisyX/DaisyXmusic
$ cd DaisyXMusic
# Upgrade sources
# Install All Requirements 
$ pip3 install -U -r requirements.txt
# Fork This Repo and fill config.py vars with your own values.Then Start The Bot
$ python3 -m DaisyXMusic
```

### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/play <reply to audio>` - play replied file
- `/dplay <song name>` - play song you requested via deezer
- `/splay <song name>` - play song you requested via jio saavn
- `/ytplay <song name>`: Directly play song via Youtube Music
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/deezer <song name>` - download songs you want quickly via deezer
- `/saavn <song name>` - download songs you want quickly via saavn
- `/video <song name>` - download videos you want quickly

#### Admins only.
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/admincache` - Refresh admin list
- `/musicplayer [on/off]` - Enable/Disable Music Player

### Commands for Channel Music Play 🛠
For linked group admins only:
- `/cplay <song name>` - play song you requested
- `/cplay <reply to link>` - play replied youtube link
- `/cplay <reply to audio>` - play replied file
- `/cdplay <song name>` - play song you requested via deezer
- `/csplay <song name>` - play song you requested via jio saavn
- `/cplaylist` - Show now playing list
- `/cccurrent` - Show now playing
- `/cplayer` - open music player settings panel
- `/cpause` - pause song play
- `/cresume` - resume song play
- `/cskip` - play next song
- `/cend` - stop music play
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



### Inspiration
- [Callsmusic](http://github.com/callsmusic/callsmusic)
- [tgvc-userbot](https://github.com/callsmusic/tgvc-userbot)

This project is inspired on the hard work done by [Rojserbest](http://github.com/rojserbest). Without his hardwork daisyxmusic won't exist. 
Also DaisyXmusic is inspired by many opensource bots and userbots

### Don't Edit This Part

#### Developers &Contribtors
- [InukaASiTH](https://github.com/InukaAsith): Dev/Owner
- [Technical-Hunter](https://github.com/Technical-Hunter): Dev/Owner
- [lucifeermorningstar](https://github.com/lucifeermorningstar): Dev/Owner
- [Rojserbest](http://github.com/rojserbest): Dev of callsmusic
- [Wrench](https://github.com/EverythingSuckz/): Dev
- [Bemro](https://github.com/bemroofficial): Dev
- [QueenArzoo](https://github.com/QueenArzoo): Dev
- [HamkerCat](https://github.com/thehamkercat/)
- [AnjanaMadu](https://github.com/AnjanaMadu): 
- [ImJanindu](https://github.com/ImJanindu): 
- [MARSHALX](https://github.com/MarshalX): TgCalls
- [Original Repo owners](https://github.com/CallsMusic/CallsMusic)


## Copyright & License 👮

 - Copyright (C) 2020 - 2021 by [TeamDaisyX](github.com/teamdaisyx) ❤️️
 - Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/TeamDaisyX/DaisyXMusic/blob/master/LICENSE)
    
DaisyXMusic is Free Software: You can use, study share and improve it at your will. Specifically you can redistribute and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.    
## Made with ♥️ by [TeamDaisyX](https://github.com/TeamDaisyX)
