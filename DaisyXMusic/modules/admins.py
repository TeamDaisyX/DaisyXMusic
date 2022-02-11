from asyncio import QueueEmpty

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types.input_stream import AudioPiped

from DaisyXMusic.function.admins import set
from DaisyXMusic.helpers.channelmusic import get_chat_id
from DaisyXMusic.helpers.decorators import authorized_users_only, errors
from DaisyXMusic.helpers.filters import command, other_filters
from DaisyXMusic.services.pytgcalls import pytgcalls
from DaisyXMusic.services.queues import queues

ACTV_CALLS = []


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❗ Nothing is playing!")
    else:
        await pytgcalls.pause_stream(chat_id)
        await message.reply_text("▶️ Paused!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❗ Nothing is paused!")
    else:
        await pytgcalls.resume_stream(chat_id)
        await message.reply_text("⏸ Resumed!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    for x in pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❗ Nothing is streaming!")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await pytgcalls.leave_group_call(chat_id)
        await message.reply_text("❌ Stopped streaming!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    for x in pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("❗ Nothing is playing to skip!")
    else:
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            await pytgcalls.leave_group_call(chat_id)
        else:
            await pytgcalls.change_stream(
                chat_id,
                AudioPiped(
                    queues.get(chat_id)["file"],
                ),
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Skipped **{skip[0]}**\n- Now Playing **{qeue[0][0]}**")


@Client.on_message(command("mute") & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    chat_id = get_chat_id(message.chat)
    result = await pytgcalls.mute_stream(chat_id)
    await message.reply_text("✅ Muted")
    if mute:
        result == 0
    else:
        await message.reply_text("❌ Already muted")
    if not mute:
        result == 1
    else:
        await message.reply_text("❌ Not in call")


@Client.on_message(command("unmute") & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    chat_id = get_chat_id(message.chat)
    result = await pytgcalls.unmute_stream(chat_id)
    await message.reply_text("✅ Unmuted")
    if unmute:
        result == 0
    else:
        await message.reply_text("❌ Not muted")
    if not unmute:
        result == 1
    else:
        await message.reply_text("❌ Not in call")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")
