""" Team7 RiZoeL || जय श्री राम 🚩"""

import os, sys, datetime, time
from Team7.functions import get_time 
from Team7 import start_time, Team7Users, Owner, Devs 
from .import Alive_pic, Alive_buttons
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup
from seven.db import gban_db, users_db, report_db


@Client.on_message(filters.user(Team7Users) & filters.command(["ping"], ["!", "?", "/", "."]))
async def ping(_, e: Message):
   start = datetime.datetime.now()
   uptime = await get_time((time.time() - start_time))
   Fuk = await e.reply_text("**Pong !!**")
   end = datetime.datetime.now()
   ms = (end-start).microseconds / 1000
   await Fuk.edit_text(f"ᴘɪɴɢ: `{ms}` ᴍs \n  - ᴜᴘᴛɪᴍᴇ: `{uptime}`")


@Client.on_message(filters.user(Team7Users) & filters.command(["alive"], ["!", "?", "/", "."]))
async def alive(_, e: Message):
    if ".jpg" in Alive_pic or ".png" in Alive_pic:
       await e.reply_photo(Alive_pic, caption=Alive_msg, reply_markup=InlineKeyboardMarkup(Alive_buttons))
    if ".mp4" in Alive_pic or ".MP4," in Alive_pic:
       await e.reply_video(Alive_pic, caption=Alive_msg, reply_markup=InlineKeyboardMarkup(Alive_buttons))


@Client.on_message(filters.user(Owner) & filters.command(["restart"], ["!", "?", "/", "."]))
@Client.on_message(filters.user(Devs) & filters.command(["restart"], ["!", "?", "/", "."]))
async def restart(Team7: Client, message: Message):
     reboot_text = "**Re-starting** \n\n__Wait For A While To Use it Again__ "
     await message.repky(reboot_text)
     try:
         Team7.disconnect()
     except Exception as e:
         pass
     args = [sys.executable, "-m", "Team7"]
     os.execl(sys.executable, *args)
     quit()


@Client.on_message(filters.command("id"))
async def getid(client: Client, message: Message):
    chat = message.chat
    your_id = message.from_user.id
    reply = message.reply_to_message
    text = f"**Your ID:** `{your_id}`\n"
    text += f"**Chat ID:** `{chat.id}`\n\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user = await client.get_users(split)
            text += f"{user.first_name}'s ID: `{user.id}`\n"

        except Exception:
            return await message.reply_text("This user doesn't exist.", quote=True)

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
      try:
        user = await client.get_users(reply.from_user.id)
        text += f"**{user.first_name}'s ID:** `{reply.from_user.id}` \n\n"
      except:
        text += f"**Replied User ID:** `{reply.from_user.id}` \n\n"

    if reply and reply.forward_from_chat:
        text += f"The forwarded channel, {reply.forward_from_chat.title}, has an id of `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ID of the replied chat/channel, is `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
       text,
       disable_web_page_preview=True,
       parse_mode=ParseMode.MARKDOWN,
   )


# stats
@Client.on_message(filters.user(Team7Users) & filters.command(["stats"], ["!", "?", "/", "."]))
async def stats_(_: Client, e: Message):
    stat = "**Red7 - Scanner's current stats** \n\n"
    stat += f"  **• Total Devs:** `{users_db.dev_count()}` \n"
    stat += f"  **• Total Red-Sudo:** `{users_db.sudo_count()}` \n"
    stat += f"  **• Total Bots:** `{users_db.bot_count()}` \n\n"
    stat += f"  **• Total scanned users:** `{gban_db.scan_count()}` \n"
    stat += f"  **• Total reported users:** `{report_db.report_count()}` \n"
    
    if ".jpg" in Alive_pic or ".png" in Alive_pic:
       await e.reply_photo(Alive_pic, caption=stat, reply_markup=InlineKeyboardMarkup(Alive_buttons))
    if ".mp4" in Alive_pic or ".MP4," in Alive_pic:
       await e.reply_video(Alive_pic, caption=stat, reply_markup=InlineKeyboardMarkup(Alive_buttons))
