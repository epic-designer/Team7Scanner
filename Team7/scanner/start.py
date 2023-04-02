""" Team7 || RiZoeL """

import platform 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Team7.core import start_msg, start_buttons, __version__, Channel, Support 
from Team7.database import users_db
from . import Team7Users 
from RiZoeLX.functions import delete_reply
from pyrogram import __version__ as pyro_vr
from RiZoeLX import __version__ as rizoelx_vr

PIC = "https://telegra.ph//file/57781115c5b6cc7ea23bc.jpg"
GRP_PIC = "https://telegra.ph//file/57781115c5b6cc7ea23bc.jpg"

@Client.on_message(filters.command(["start"], ["!", "/"]))
async def start_(_, message: Message):
    if message.from_user.id == message.chat.id:
       msg = start_msg.format(message.from_user.mention)
       try:
         await message.reply_photo(PIC, caption=msg, reply_markup=InlineKeyboardMarkup(start_buttons))
       except:
         await message.reply_text(msg, reply_markup=InlineKeyboardMarkup(start_buttons))
    else:
       try:
         await message.reply_video(GRP_PIC, caption="Contact me in PM to start :) ")
       except:
         await message.reply_text("Contact me in PM to start :) ")

@Client.on_message(filters.user(Team7Users) & filters.command(["Team7", "t7", "seven"], ["!", "/"]))
async def team7bruh_(_, message: Message):
   hui = await message.reply("!.....")
   final_text = "**Team7 Info** \n"
   final_text += "<===================> \n"
   user = message.from_user
   await hui.edit_text("getting user details...")
   final_text += f"  **Your Name:** {user.first_name} \n"
   final_text += f"  **Your ID:** `{user.id}` \n"
   if users_db.check_owner(user.id):
      final_text += f"  **Your Rank:** Owner 🔱 \n"
   elif users_db.check_dev(user.id):
      final_text += f"  **Your Rank:** Dev ⚜️ \n"
   else:
      final_text += f"  **Your Rank:** Sudo 〽️ \n"
   hui.edit_text(".....!")
   hui.edit_text("fetching versions...")
   final_text += f"  **Team7-scanner Ver:** `{__version__}` \n"
   final_text += f"  **Python ver:** `{platform.python_version()}` \n"
   final_text += f"  **pyrogram ver:** `{pyro_vr}` \n"
   final_text += f"  **pyRiZoeLX ver:** `{rizoelx_vr}` \n"
   hui.edit_text("...!...")
   hui.edit_text("checking ping...")
   final_text += "<===================> \n\n"
   hui.edit_text("......")
   final_text += "**Powered By Team7!** \n"
   hui.edit_text("Team7 is alive....")
   hui.edit_text("Team7 Scanner....")
   hui.edit_text("Ready....")
   buttons = [ [
              InlineKeyboardButton(
                    "× Alive", callback_data="alive"),
              InlineKeyboardButton(
                    "Ping ×", callback_data="ping")
             ], [
              InlineKeyboardButton(
                    "× stats", callback_data="stats"),
                    InlineKeyboardButton(
                    "× Channel ", url="https://github.com/MrRizoel/Team7Scanner")
             ], [
              InlineKeyboardButton(
                    "× Channel ", url=f"https://t.me/{Channel}"),
              InlineKeyboardButton(
                    " Support ×", url=f"https://t.me/{Support}")
             ],
             ]
   await hui.delete()
   await message.reply_photo(PIC, caption=final_text, reply_markup=InlineKeyboardMarkup(buttons))
    
