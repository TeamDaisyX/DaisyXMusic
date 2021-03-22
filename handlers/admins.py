import queue

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

import queues
import cache.admins

from config import BOT_NAME as BN
from helpers.filters import command
from helpers.wrappers import errors, admins_only, nonadmin


@Client.on_message(command(["pause", "p"]))
@errors
@admins_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**{BN} :**❕ Nothing is playing.")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :** ⏸ Paused.")

@Client.on_message(command(["pause", "p"]))
@errors
@nonadmin
async def pausee(_, message: Message):
    await message.reply_text(f"**{BN} :** 🤐 Only Admins & Sudo Users Can do that.")


@Client.on_message(command(["resume", "r"]))
@errors
@admins_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text(f"**{BN} :**❕ Nothing is paused.")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :** ▶️ Resumed.")


@Client.on_message(command(["resume", "r"]))
@errors
@nonadmin
async def re(_, message: Message):
    await message.reply_text(f"**{BN} :** 🤐 Only Admins & Sudo Users Can do that.")


@Client.on_message(command(["end", "s"]))
@errors
@admins_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :**❕ Nothing is streaming.")
    else:
        try:
            queues.clear(message.chat.id)
        except queue.Empty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :** ⏹ Stopped streaming.")

@Client.on_message(command(["end", "s"]))
@errors
@nonadmin
async def pausee(_, message: Message):
    await message.reply_text(f"**{BN} :** 🤐 Only Admins & Sudo Users Can do that.")


@Client.on_message(command(["skip", "next"]))
@errors
@admins_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :**❕ Nothing is playing to skip.")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(message.chat.id, queues.get(message.chat.id)["file_path"])

        await message.reply_text(f"**{BN} :** ⏩ Skipped the current song.")


@Client.on_message(command(["skip", "next"]))
@errors
@nonadmin
async def pausee(_, message: Message):
    await message.reply_text(f"**{BN} :** 🤐 Only Admins & Sudo Users Can do that.")


@Client.on_message(command("admincache"))
@errors
@admins_only
async def admincache(_, message: Message):
    cache.admins.set(
        message.chat.id,
        [member.user for member in await message.chat.get_members(filter="administrators")]
    )
    await message.reply_text(f"**{BN} :** ❇ Admin cache refreshed!")


@Client.on_message(command("admincache"))
@errors
@nonadmin
async def pausee(_, message: Message):
    await message.reply_text(f"**{BN} :** 🤐 Only Admins & Sudo Users Can do that.")
