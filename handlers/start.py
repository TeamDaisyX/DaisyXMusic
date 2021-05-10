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
        f"""☬ Hai {message.from_user.first_name} welcome to 𝑭𝑯 𝑴𝑼𝑺𝑰𝑲 ☬\n
        𝑭𝑯 𝑴𝑼𝑺𝑰𝑲 adalah Bot Music yang dapat memutar lagu di Group anda.
        Saya memiliki fitur :
        ┏━━
        ✦҈͜͡➳ Memutar musik.
        ✦҈͜͡➳ Mendownload lagu.
        ✦҈͜͡➳ Mencari lagu yang ingin kamu putar atau download.
        ┗━━
        👨🏻‍💻 Managed with by : [ᴘᴀᴛʀɪᴄᴋ](https://t.me/SweetKillerBot)\n\n
        Do you want me to play music in your Telegram groups'voice chats? Please click the \'User Manual\' button below to know how you can use me.\n\n The Assistant must be in your group to play music in the voice chat of your group.\n\n More info & commands mentioned in the [User Manual](https://telegra.ph/Daisy-X-04-19)\n\nA project by @TeamDaisyX""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 User Manual 📜", url="https://telegra.ph/Daisy-X-04-19")
                  ],[
                    InlineKeyboardButton(
                        "Join Group", url="https://t.me/gabutgabutonline"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/katasecangkir"
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
                        "👨🏻‍💻 Owner", url="https://t.me/SweetKillerBot")
                ]
            ]
        )
   )

