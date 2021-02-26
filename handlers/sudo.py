from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import sira
from helpers.filters import sudoers
from helpers.wrappers import errors


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
    & sudoers
)
@errors
async def stop(client: Client, message: Message):
    if message.chat.id in tgcalls.playing:
        tgcalls.playing.remove(message.chat.id)

    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
