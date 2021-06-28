# Copyright (C) 2021 TeamDaisyX


# This file is part of Daisy (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot




# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics.....")
    query = message.text
    if not query:
        await lel.edit("`What I am Supposed to find `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try `.glyrics`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
