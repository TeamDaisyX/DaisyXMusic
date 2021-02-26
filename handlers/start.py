from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yes.", switch_inline_query_current_chat=""
                    )
                ],
                [
                    InlineKeyboardButton(
                        "No, close this.", callback_data="close"
                    )
                ]
            ]
        )
    )
