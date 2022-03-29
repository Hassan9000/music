import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = 10238487
API_HASH = "3aca0ff23fde23626728aeac9b33188b"
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "$")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
