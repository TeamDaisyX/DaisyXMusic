from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
🤖Hᴇʏ, ɪ'ᴍ ᴠᴄ ʙᴏᴛ❤️🔥
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. 
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!
/help - to get commands

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ✅", url="https://t.me/Itz_me_cyberking")
                  ],[
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ🔥", url="https://t.me/BONDOFBESTIZZ"
                    ),
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇ🛠", url="https://t.me/INCREDIBLE_SPAM_BOT"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕Aᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/BESTIES_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
