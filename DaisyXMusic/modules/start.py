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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hallo 👋 aku bot untuk pemutar music di group , invite aku ke group kamu dan jadikan admin untuk memutar music dan jangan lupa menambahkan asisten ku @lifeisuckx untuk info cara mengunakan bot klik < cara mengunakan bot > di bawah""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara menggunakan bot 📜", url="https://telegra.ph/command-XVII-MUSIC-04-23"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍💻 Updates 👨‍💻", url="https://t.me/owner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Chat 🎙️", url="https://t.me/loveiswarXVII"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**🔴 Music player is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/loveiswarXVII"
                    )
                ]
            ]
        ),
    )
