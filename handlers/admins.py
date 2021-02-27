from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import sira
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)


@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    sira.task_done(chat_id)

    if sira.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, sira.get(chat_id)["file_path"]
        )
