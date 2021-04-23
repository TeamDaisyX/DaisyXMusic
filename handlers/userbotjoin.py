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
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>JADIIN ADMIN DULU SAYANG</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "ROBOT MUSIC"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>OK SUDAH JOIN</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>User {user.first_name} MASUKKAN @musicsrobot_bot dan @robotassisten DULU SAYANG! JANGAN DIKICK DARI GRUB MASUK DAFTAR BLOKIR."
            "\n\nOr MASUKKAN @musicsrobot_bot ke GRUB ANDA dan COBA LAGI SAYANG</b>",
        )
        return
    await message.reply_text(
            "<b>OK SUDAH JOIN</b>",
        )
