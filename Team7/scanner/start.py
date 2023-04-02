""" Team7 || RiZoeL """

from pyrogram import Clients, filters
from pyrogram.types import Message, InlineKeyboardMarkup
from Team7.core import start_msg, start_buttons

PIC = ""
GRP_PIC = ""

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
