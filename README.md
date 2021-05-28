<h1 align="centre">DAISYXMUSIC V4.0 🎵</h1>

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
- Deezer,Youtube & Saavn playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play

## 🚀 Deployment

### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/teamdaisyx/DaisyXMusic)

Get pyrogram (p)  `SESSION` from here:
[![Run on Repl.it](https://repl.it/badge/github/SpEcHiDe/GenerateStringSession)](https://repl.it/@SpEcHiDe/GenerateStringSession)

### ⚔ Self-hosting (For Devs) 
```sh
# Install Git First (apt-instll git)
$ git clone https://github.com/TeamDaisyX/DaisyXmusic
$ cd DaisyXMusic
# Upgrade sources
# Install All Requirements 
$ pip(3) install -r requirements.txt
# Rename example.env to local.env and fill
$ npm i -g npm
# Start Bot 
$ python(3) -m DaisyXMusic
```

### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/play <reply to audio>` - play replied file
- `/dplay <song name>` - play song you requested via deezer
- `/splay <song name>` - play song you requested via jio saavn
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

### Credits
Don't edit this part

#### Special Credits
- [Rojserbest](http://github.com/rojserbes): Callsmusic Developer

This bot is based on the original work done by [Rojserbest](http://github.com/rojserbest). Without his hardwork daisyxmusic won't exist. 
DaisyXmusic is a modified version of [Callsmusic](https://github.com/callsmusic/callsmusic) for fit the needs of @DaisyXbot users

#### Contribtors
- [InukaASiTH](https://github.com/InukaAsith): Dev
- [Rojserbest](http://github.com/rojserbes): Dev
- [Wrench](https://github.com/EverythingSuckz/): Dev
- [QueenArzoo](https://github.com/QueenArzoo): Dev
- [lucifeermorningstar](https://github.com/lucifeermorningstar): Dev
- [AuraXNetwork](https://github.com/AuraXNetwork/AuraXMusicBot)
- [Hamker Cat](https://github.com/thehamkercat/)
- [Anjana-Ma](https://github.com/Anjana-Ma): 
- [ImJanindu](https://github.com/ImJanindu): 
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls
- [Original Repo owners](https://github.com/suprojects/CallsMusic)
