from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
