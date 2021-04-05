import os
from os import path
import requests
import aiohttp
import youtube_dl
from pyrogram import Client
from pyrogram.types import Message, Voice
from youtube_search import YoutubeSearch
from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("ytp") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("🔄 **Processing**...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    lel = await message.reply('🔎 **Finding** the song...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    
    if url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("❗ You did not give me anything to play!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#⃣ **Queued** at position {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://telegra.ph/file/a4fa687ed647cfef52402.jpg",
        caption="▶️ **Playing** here the song requested by {}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
