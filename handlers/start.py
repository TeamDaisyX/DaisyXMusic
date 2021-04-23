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
        f"""Hello Friends, 
Ini adalah bot music yang membantumu untuk memutar music di VOICE CHAT GRUB anda. 

NB : Maaf jika ada kekurangan didalam bot ini.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                
                 [
                    InlineKeyboardButton(
                        "⚒️ OWNER 🛠️", url="https://t.me/justthetech")
                  ],[
                    InlineKeyboardButton(
                        "GRUB I 👥", url="https://t.me/randomcryptoid"
                    )
                    InlineKeyboardButton(
                        "GRUB II 👥", url="https://t.me/gcwoah"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "CHANNEL 🚀", url="https://t.me/pejuangairdrops"
                    
                    )
                  ],[
                    InlineKeyboardButton(
                        "DAFTAR PERINTAH ✍️", url="https://telegra.ph/ROBOT-04-23-2")
                 ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 ROBOT MUSIC BOT ONLINE **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Grub👥", url="https://t.me/randomcryptoid")
                ]
            ]
        )
   )

