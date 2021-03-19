from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

import callsmusic

import converter
import youtube
import queues

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError
from helpers.filters import command, other_filters
from helpers.wrappers import errors


@Client.on_message(command("play") & other_filters)
@errors
async def play(_, message: Message):
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None

    res = await message.reply_text("🔄 Processing...")

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {audio.duration / 60} minute(s)"
            )

        file_name = audio.file_unique_id + "." + (
            audio.file_name.split(".")[-1] if not isinstance(audio, Voice) else "ogg"
        )
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    else:
        messages = [message]
        text = ""
        offset = None
        length = None

        if message.reply_to_message:
            messages.append(message.reply_to_message)

        for _message in messages:
            if offset:
                break

            if _message.entities:
                for entity in _message.entities:
                    if entity.type == "url":
                        text = _message.text or _message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset in (None,):
            await res.edit_text("❕ You did not give me anything to play.")
            return

        url = text[offset:offset + length]

        file_path = await converter.convert(youtube.download(url))

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = queues.add(message.chat.id, file_path)
        await res.edit_text(f"#️⃣ Queued at position {position}.")
    else:
        await res.edit_text("▶️ Playing...")
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path, 48000, callsmusic.pytgcalls.get_cache_peer())
