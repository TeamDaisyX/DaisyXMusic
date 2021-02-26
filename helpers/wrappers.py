from typing import Callable, Coroutine

from pyrogram import Client
from pyrogram.types import Message


def errors(func):
    async def wrapper(client: Client, message: Message):
        try:
            await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")
    return wrapper
