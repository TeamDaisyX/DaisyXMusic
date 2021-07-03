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
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Pengaturan Utama**
1) Membuat bot admin (Group dan di channel jika menggunakan cplay)
2) Mulai obrolan suara
3) Coba /play [nama lagu] pertama kali oleh admin
*) Jika userbot bergabung nikmati musik, Jika tidak tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi
**Untuk Channel Music Play**
1) Jadikan saya admin saluran Anda
2) Kirim /userbotjoinchannel di grup tertaut
3) Sekarang kirim perintah di grup tertaut
**Beberapa Command**
**◎› Memainkan Lagu 🎧**
• /play <nama lagu> : putar lagu yang Anda minta
• /play <url youtube> : Putar lagu melalui balasan url youtube
• /play <balas ke audio> : putar file balasan
• /dplay <nama lagu> : putar lagu yang Anda minta melalui deezer
• /splay <nama lagu> : putar lagu yang Anda minta melalui jio saavn
**◎› Playback ⏯**
• /player: buka panel pengaturan pemutar musik
• /skip: putar lagu berikutnya
• /pause: jeda pemutaran lagu
• /resume: melanjutkan pemutaran lagu
• /end: hentikan pemutaran musik
• /current: Tampilkan sedang diputar
• /playlist: Tampilkan daftar yang sedang diputar
__**Cmd player dan semua cmd lain kecuali**__ /play, /current __**dan**__ /playlist __**hanya untuk admin grup**__
""",
        
f"""
**◎› Putar Musik Di Channel 📮**
⚪️ Hanya untuk admin grup tertaut:
• /cplay [song name] - putar lagu yang Anda minta
• /cdplay [song name] - putar lagu yang Anda minta via deezer
• /csplay [song name] - putar lagu yang Anda minta via jio saavn
• /cplaylist - Perlihatkan daftar yang dimainkan
• /cccurrent - Perlihatkan yang diputar sekarang
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - lanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - stop pemutaran lagu
• /userbotjoinchannel - Undang asisten ke chat kamu
saluran Channel juga dapat digunakan sebagai pengganti c ( /cplay = /channelplay )
⚪️ Jika Anda tidak suka bermain di grup tertaut:
1) Dapatkan ID saluran Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Saluran dengan izin penuh
4) Tambahkan @{ASSISTANT_NAME} ke saluran sebagai admin.
5) Cukup kirim perintah di grup Anda.
""",

f"""
**◎› More Info 📲**
• /admincache: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
• /userbotjoin: Undang @{ASSISTANT_NAME} Userbot ke obrolan Anda
**◎› 📝 Command Khusus buat pengguna sudo**
 • /userbotleaveall - Keluarkan asisten musik dari semua obrolan chat
 • /broadcast <balas ke pesan> - global brodcast membalas pesan ke semua obrolan
 • /pmpermit [on/off] - enable/disable pesan pmpermit 
__Pengguna Sudo dapat menjalankan perintah apa pun di grup mana pun__
◎› Owner Project: [Yunus Zend](https://t.me/ZendYNS)
◎› Source Code: [Click Here](https://github.com/Yunus-ZEND/VC-MusicINDO)
"""
      ]

# Editor by Creator And Contributor
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
