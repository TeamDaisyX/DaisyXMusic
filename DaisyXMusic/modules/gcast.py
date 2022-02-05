import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from DaisyXMusic.config import SUDO_USERS
from DaisyXMusic.services.callsmusic.callsmusic import client as USER


@Client.on_message(filters.command(["broadcast"]))
async def broadcast(_, message: Message):
    sent = 0
    failed = 0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Starting a broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("Please Reply to a Message to broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent + 1
                await wtf.edit(
                    f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats"
                )
                await asyncio.sleep(3)
            except:
                failed = failed + 1
                # await wtf.edit(f"`broadcasting...` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats")

        await message.reply_text(
            f"`Broadcast Finished ` \n\n**Sent to:** `{sent}` Chats \n**Failed in:** {failed} Chats"
        )
