from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN


app = Client(
    "my_account",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)


if __name__ == "__main__":
    import os
    import sys
    from threading import Thread
    from pyrogram import idle, filters
    from pyrogram.handlers import MessageHandler
    from config import SUDO_USERS, BOT_NAME

    def stop_and_restart():
        app.stop()
        os.system("git pull")
        os.execl(sys.executable, sys.executable, *sys.argv)

    @app.on_message(
        filters.command(["restart", "update"])
        & filters.group
        & ~ filters.edited
    )
    @errors
    @admins_only
    def restart(client, message):
        message.reply_text(f"**{BOT_NAME} :** Restarting and pulling latest codes...")
        Thread(
            target=stop_and_restart
        ).start()

    @app.on_message(
        filters.command(["restart", "update"])
        & filters.private
        & ~ filters.edited
    )
    @errors
    @admins_only
    def restart(client, message):
        message.reply_text(f"**{BOT_NAME} :** Restarting and pulling latest codes...")
        Thread(
            target=stop_and_restart
        ).start()

    app.start()
    idle()
