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



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hallo 👋 perkenalkan saya rosewan! Bisa memulai saya di Voice Obrolan Telegram Groups. dan ini versi music terbaru bahkan lebih banyak menunya dari music sebelumnya!\n\n🔴 gunakan tombol perintah\' 📜 Perintah Pengguna 📜 \' gunakan tombol dibawah untuk mengetahui perintah.\n\n masukan asistan music bot kedalam grup jika gagal hubungi admin \n\n🔴 info dan commands menu [perintah pengguna](https://telegra.ph/Musicwan-04-25)\n\nA Created By @RI024""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Perintah pengguna 📜", url="https://telegra.ph/Musicwan-04-25")
                  ],[
                    InlineKeyboardButton(
                        "☕ Join Grup ☕", url="https://t.me/antigabutbrothers"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "**Owner**", url="https://t.me/RI024"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☕ Join grup ☕", url="https://t.me/antigabutbrothers")
                ]
            ]
        )
   )

