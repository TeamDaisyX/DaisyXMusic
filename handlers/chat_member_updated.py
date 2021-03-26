from pyrogram import Client
from pyrogram.types import ChatMemberUpdated

from cache import admins as cache


@Client.on_chat_member_updated()
async def chat_member_updated(_, chat_member_updated: ChatMemberUpdated):
    chat = chat_member_updated.chat.id
    new = chat_member_updated.new_chat_member

    if new.can_manage_voice_chats:
        if new.user.id not in cache.admins[chat]:
            cache.admins[chat].append(new.user.id)
    else:
        if new.user.id in cache.admins[chat]:
            cache.admins[chat].remove(new.user.id)
