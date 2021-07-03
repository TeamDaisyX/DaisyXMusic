# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 🗿 [{}](tg://user?id={})!**\n\n🤖 saya 𝙧𝙞𝙯𝙚𝙭 𝙢𝙪𝙨𝙞𝙘 aku adalah bot music \n \n ━━━━━━━━━━━━━━━━━━━━━━━━━ \n \n saya dapat memutar lagu di voice chat group dan di channel kamu \n \n ketik /help untuk informasi lengkap saya \n \n ━━━━━━━━━━━━━━━━━━━━━━━━━ managed by @rizexx"
      HELP_MSG = [
        ".",
f"""
**✨Hii, selamat datang kembali di {PROJECT_NAME}

⚪️ {PROJECT_NAME} bisa memutar musik di grup voice chat dan di channel kamu.


⚪️ assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**✨pengaturan untuk grup**

1) bot music wajib jadi admin dan diberi izin untuk mengelola obrolan suara.
2) nyalaiin vcg atau voice chat grup lu dulu ngab sebelum request musik.
3) lalu ketik /play [judul lagu] untuk memutar musik.
*) jika asisten bergabung ke vcg silahkan menikmati musiknya pantek, jika tidak, tambahkan @ { ASSISTANT_NAME } ke dalam grup lalu coba lagi.

**pengaturan untuk channel**
1) jadiian gua admin di channel lu ngab
2) ketik /userbotjoinchannel di grup yang udah asyik dengan channelnya.
3) lalu ketikkan perintah dibawah ini di dalam grup yang menuju ke saluran
""",
f"""
**perintah untuk memutar lagu**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
