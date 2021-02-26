"""
To prevent conflict with built-in modules, using "sira", the Greek word for "queue".
"""
from asyncio.queues import QueueEmpty
from typing import Dict, Union
import asyncio


queues: Dict[str, asyncio.Queue] = {}


async def add(chat_id: Union[str, int], file_path: str) -> int:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id not in queues:
        queues[chat_id] = asyncio.Queue()

    await queues[chat_id].put(
        {
            "file_path": file_path
        }
    )
    return queues[str(chat_id)].qsize()


def get(chat_id: Union[str, int]) -> Union[Dict[str, str], None]:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id in queues:
        try:
            return queues[chat_id].get_nowait()
        except asyncio.queues.QueueEmpty:
            return None


def is_empty(chat_id: Union[str, int]) -> Union[bool, None]:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id in queues:
        return queues[chat_id].empty()
    else:
        return True


def task_done(chat_id: Union[str, int]) -> None:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass


def clear(chat_id: Union[str, int]) -> None:
    if isinstance(chat_id, int):
        chat_id = str(chat_id)

    if chat_id in queues:
        if queues[chat_id].empty():
            raise QueueEmpty("The queue is empty.")
        else:
            queues[chat_id]._queue = []
    else:
        raise QueueEmpty("The queue is empty.")
