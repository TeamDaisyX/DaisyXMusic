from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**Hêllẞø†:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
