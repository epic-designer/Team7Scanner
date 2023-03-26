""" Team7 || RiZoeL ""*

# Imports
import platform
from pyrogram import idle, __version__ as pyro_vr
from RiZoeLX import __version__ as rizoelx_vr
from .version import __version__


def StartScanner():


    print(f"[Team7 INFO]: Python Version - {platform.python_version()}")
    print(f"[Team7 INFO]: SpamX Version - {__version__}")
    print(f"[Team7 INFO]: pyRiZoeLX Version - {rizoelx_vr}")
    print(f"[Team7 INFO]: Pyrogram Version - {pyro_vr}")
    print("""\n\n
     Team7 Scanner started successfully!
    """)
    idle()
