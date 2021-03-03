from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only

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

def stop_and_restart():
    Client.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(
    filters.command("restart")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def restart(client, message):
    message.reply_text("**Hêllẞø†:** 🔄 Restarted And Updated To Latest Codes.")
    Thread(
        target=stop_and_restart
    ).start()

Client.start()
idle()
