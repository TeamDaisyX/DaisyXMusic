from pyrogram import filters
from config import SUDO_USERS

sudoers = filters.user(SUDO_USERS)
