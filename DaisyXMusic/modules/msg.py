# nelover music (Telegram bot project )
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

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "** هلاا [{}](tg://user?id={})!**\n\n  بوت الاغاني المقدم من سورس نيلوفر ، كل الي عليك تضيف البوت والحساب المساعد وترفعهم مشرف ، للمزيد من المعلومات اضغط /help"
    HELP_MSG = [
        ".",
        f"""
**Hey هلابيك من جديد {PROJECT_NAME}

⚪️ {PROJECT_NAME} يستطيع تشغيل الاغاني في المكالمات الجماعيه

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\n اضغط "التالي" للمزيد من التعليمات**
"""
        f"""
**Setting up**

1) ارفع البوت والحساب المساعد مشرف
2) ابدئ مكالمه جماعيه
3) ارسل اغنيه او رابط يوتيوب او بصمه و رد عليها ب play/


""",
        f"""
**Commands**

**=>> تشغيل الأغاني 🎧**

- /play: يشغل الاغنيه المطلوبه
- /play [رابط يوتيوب] : يشغل الاغنيه من الرابط المطلوب

**=>> المشغل ⏯**

- /player: يظهر اعدادات المشغل
- /skip: يتخطى الاغنيه الحاليه
- /pause: ايقاف الاغنيه مؤقتاً
- /resume: استئناف تشغيل الاغنيه
- /end: ايقاف تشغيل الاغنيه

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
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

""",
    ]
