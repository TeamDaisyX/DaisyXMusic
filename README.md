<h1 align="centre"> DAISYXMUSIC V5.5 🎵 </h1> 

### A bot that can play music on Telegram Group and Channel Voice Chats
#### POWERED BY [PYTGCALLS](https://github.com/pytgcalls/pytgcalls)
### Available on telegram as [@DaisyXbot](https://t.me/daisyxbot)

<p align="center">
  <img src="https://telegra.ph/file/dd04b1968f1bc1169d162.jpg">
</p>

> ⭐️ Thanks to everyone who starred DaisyXMusic, That is the greatest pleasure we have !

<h2> Features 🔥 </h2>

- Thumbnail Support
- Playlist Support
- Current playback support
- Showing track names when skipping
- Zero downtime, Fully Stable
- Youtube, Local & Saavn playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play

## 🚀 Deployment

### 💜 Heroku/Railway

[![Deploy+on+Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TeamDaisyX/DaisyXMusic)

[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/TeamDaisyX/DaisyXMusic&envs=SESSION_NAME,BOT_TOKEN,BOT_USERNAME,BOT_NAME,SUPPORT_GROUP,PROJECT_NAME,ARQ_API_KEY,ASSISTANT_NAME,BG_IMAGE,UPDATES_CHANNEL,API_ID,API_HASH,SUDO_USERS,DURATION_LIMIT)

• Get pyrogram (p)  `SESSION` from here:

[![Run on Repl.it](https://repl.it/badge/github/SpEcHiDe/GenerateStringSession)](https://repl.it/@SpEcHiDe/GenerateStringSession)

### ⚔ Self-hosting (For Devs) 
```sh
# Install Git First (apt-instll git)
$ git clone https://github.com/TeamDaisyX/DaisyXmusic
$ cd DaisyXMusic
# Upgrade sources
# Install All Requirements 
$ pip3 install -r requirements.txt
# Rename example.env to local.env and fill
$ npm i -g npm
# Start Bot 
$ python3 -m DaisyXMusic
```

[Watch Tutorial on hosting DaisyXMusic on VPS](https://youtu.be/MdavNbazT7Q)


### Commands for Group 🛠
#### For all in group

- `/play <song name>` - play song you requested
- `/play <reply to audio>` - play replied file
- `/splay <song name>` - play song you requested via jio saavn
- `/ytplay <song name>`: Directly play song via Youtube Music
- `/playlist` - Show now playing list
- `/current` - Show now playing
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
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

#### Authorized users & Misc
Authorized users can execute admin commands in authorized group
- `/auth <reply to user>` - Authorize User
- `/deauth <reply to user>` - DeAuthorize user
- `/admincache` - Refesh admin list


### Commands for Channel Music Play 🛠
For linked group admins only:
- `/cplay <song name>` - play song you requested
- `/cplay <reply to link>` - play replied youtube link
- `/cplay <reply to audio>` - play replied file
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
 2. Rename your group to: `Channel Music:your_channel_id`
 3. Add [@DaisyXBot](t.me/DaisyXbot) as Channel admin with full perms
 4. Add helper to channel
 5. Simply send commands in your group.


### Commands for Sudo Users ⚔️
- `/userbotleaveall` - remove assistant from all chats
- `/gcast <reply to message>` - globally brodcast replied message to all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
- You can add a custom pmpermit message by adding var `PMMSG` and adding your message through env vars (for heroku, Settings/Edit vars)

+ Sudo Users can execute any command in any groups


## Credits
DaisyXMusic is a hardwork of many people. Many contributors and open source projects (Specially callsmusic projects) helped a lot in this. 

#### Contributors
- [InukaAsith](https://github.com/InukaAsith): Dev / Owner
- [lucifeermorningstar](https://github.com/lucifeermorningstar): Dev / Owner
- [Technical-Hunter](https://github.com/Technical-Hunter): Dev / Owner
- [Hellboy-OP](https://github.com/hellboy-op)
- [Roj Serbest](http://github.com/rojserbest): Developer of callsmusic 
- [DeshadeethThisarana](https://github.com/deshadeeth-thisarana): Dev
- [Wrench](https://github.com/EverythingSuckz/): Dev
- [Bemro](https://github.com/bemroofficial): Dev
- [QueenArzoo](https://github.com/QueenArzoo): Dev
- [Anjana-Ma](https://github.com/Anjana-Ma): Dev
- [ImJanindu](https://github.com/ImJanindu): Dev
- [azimazizov9150](https://github.com/azimazizov9150): Contributor


#### Special Credits
- [Roj Serbest](http://github.com/rojserbest): Callsmusic Developer

This bot is based on the original work done by [Rojserbest](http://github.com/rojserbest). Without his hardwork daisyxmusic won t exist. 
DaisyXmusic is a modified version of [Callsmusic](https://github.com/callsmusic/callsmusic) for fit the needs of some users

- [StarkGang](https://github.com/StarkGang/)
- [SpEcHiDe](https://github.com/SpEcHiDe/)
- [The Hamker Cat](https://github.com/thehamkercat)
- [Laky(for PyTgCalls)](https://github.com/Laky-64)
- [Dan (for pyrogram)](https://github.com/delivrance)


#### Open Source codes used in this project 
- https://github.com/callsmusic/callsmusic : Source code used here as base
- https://github.com/DevsExpo/FridayUserbot/blob/master/main_startup/helper_func/basic_helpers.py : Functions from line 275 to 351
- https://github.com/TheHamkerCat/WilliamButcherBot/blob/dev/wbb/modules/music.py : From lines 170 to 178


> This project exists thanks to these awesome developers and their codes and contributions.
> And credits goes to all who supported, all who helped and API & environmental requirement package devs and all projects helped in making this project.
> Special thanks to you for using bot
