from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    lol = await message.reply("Starting Gcast")
    if message.from_user.id in SUDO_USERS:
        if not message.reply_to_message.text:
            await lol.edit("Reply to any text message to gcast sir")
            return
        msg = message.reply_to_message.text
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
            except:
                failed=failed+1
            await asyncio.sleep(3)
        await message.reply_text(f"Gcasted message to {sent} chats. Failed {failed} chats.")
