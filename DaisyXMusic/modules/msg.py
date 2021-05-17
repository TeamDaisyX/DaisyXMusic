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

class Messages():
      HELP_MSG = [
        ".",

        "**》 DAISYXMUSIC v4 《**\n\n⚪️ DAISYXMUSIC plays music in your group's voice chat as well as channel voice chats\n\n⚪️ Assistant name >> @DaisyXhelper",
        
        "**Setting up**\n\n1) Make bot admin (Group and in channel if use cplay)\n2) Start a voice chat\n3) Try /play [song name] for the first time by an admin\n*) If userbot joined enjoy music, If not add @DaisyXhelper to your group and retry\n\n**Commands**\n\n**=>> Song Playing 🎧**\n\n- /play: Play song using youtube music\n- /play [yt url] : Play the given yt url\n- /dplay: Play song via deezer\n- /splay: Play song via jio saavn\n\n**=>> Playback ⏯**\n\n- /player: Open Settings menu of player\n- /skip: Skips the current track\n- /pause: Pause track\n- /resume: Resumes the paused track\n- /end: Stops media playback\n- /current: Shows the current Playing track\n- /playlist: Shows playlist",
        
        "**=>> Channel Music Play 🛠**\n\n⚪️ For linked group admins only:\n\n- /cplay [song name] - play song you requested\n- /cdplay [song name] - play song you requested via deezer\n- /csplay [song name] - play song you requested via jio saavn\n- /cplaylist - Show now playing list\n- /cccurrent - Show now playing\n- /cplayer - open music player settings panel\n- /cpause - pause song play\n- /cresume - resume song play\n- /cskip - play next song\n- /cend - stop music play\n- /userbotjoinchannel - invite assistant to your chat\n\nchannel is also can be used instead of c ( /cplay = /channelplay )\n\n⚪️ If you donlt like to play in linked group:\n\n1) Get your channel ID.\n2) Create a group with tittle: Channel Music: your_channel_id\n3) Add @DaisyXBot as Channel admin with full perms\n4) Add @DaisyXhelper to the channel as an admin.\n5) Simply send commands in your group.",
        
        "**=>> More tools 🧑‍🔧**\n\n- /admincache: Updates admin info of your group. Try if bot isn't recognize admin\n- /userbotjoin: Invite @DaisyXhelper Userbot to your chat\n\n*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group."
      ]

START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."