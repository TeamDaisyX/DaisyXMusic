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




from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo saya, adalah music asisstan rosewan masukan saya ke grup kamu .\n\n ❗️ Rules:\n   - jangan request terus menerus menghindari erorr \n   - gunakan dengan bijak  \n\n 👉 **Jangan lupa jika ingin menambah kirim link grup saya akan membalasnya jika tidak ada halangan .**\n\n ⚠️ izin : terlebih dahulu ke admin jika ingin menggunakan atau jika ada kesalah reload ulang sama kamu\n    - jangan banned userbot di grup kamu.\n   - share informasi private tentang masalah bot\n\n")
  return                        
