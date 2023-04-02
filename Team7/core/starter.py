""" Team7 || RiZoeL """

# Imports
import platform
from pyrogram import idle, __version__ as pyro_vr
from RiZoeLX import __version__ as rizoelx_vr
from .version import __version__
from .client import Team7Scanner, assistant 
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


async def Start_assistant():
    try:
        await assistant.start()
        print("[Team7 INFO]: Scanner Assistant started")
    except Exception as a:
        print(f"[Team7 INFO]: Error {str(a)}")

async def StartScanner():
    print("[Team7 INFO]: Starting Team7 Scanner")
    try:
        await Team7Scanner.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("[Team7 INFO]: API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("[Team7 INFO]: Bot TOKEN is not valid.")
    try:
       uname = await Team7Scanner.get_me().username
       print(f"[Team7 INFO]: @{uname} is now running!")
    except:
       print("[Team7 INFO]: Scanner is now running!")

    print(f"[Team7 INFO]: Python Version - {platform.python_version()}")
    print(f"[Team7 INFO]: Tea7 Scanner Version - {__version__}")
    print(f"[Team7 INFO]: pyRiZoeLX Version - {rizoelx_vr}")
    print(f"[Team7 INFO]: Pyrogram Version - {pyro_vr}")
    print("""\n\n
     Team7 Scanner started successfully!
    """)
    await idle()
    await Team7Scanner.stop()
    print("Bot stopped.")
