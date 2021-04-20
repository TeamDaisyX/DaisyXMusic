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
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>User {user.first_name} couldn't join your group! Make sure user is not banned in group."
            "\n\nOr manually add @DaisyXhelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>helper userbot joined your chat</b>",
        )
