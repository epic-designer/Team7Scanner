""" Team7 © RiZoeL """

import pyroaddon
from pyrogram import Client
from .config import TOKEN, SESSION, API_ID, API_HASH

print("[Team7 INFO]: Defining Scanner......")
Team7Scanner = Client(
    'Team7Scanner',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="Team7.scanner")
)
print("[Team7 INFO]: Got Scanner!")

print("[Team7 INFO]: Defining Assistant......")
assistant = Client(
    'Team7Assistant',
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)
print("[Team7 INFO]: Got Assistant!")
