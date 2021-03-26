from typing import List

from pyrogram.types import Chat, User

import cache.admins


async def get_administrators(chat: Chat) -> List[User]:
    get = cache.admins.get(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        cache.admins.set(chat.id, to_set)
        return await get_administrators(chat)
