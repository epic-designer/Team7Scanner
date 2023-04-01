""" © Team7 RiZoeL """

from Team7.database import users_db

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_callback_query()
async def T7callbacks(T7: Client, callback_query: CallbackQuery):
   query = callback_query.data.lower()
   chat = callback_query.message.chat
   admin = callback_query.from_user
   message = callback_query.message
   if query == "reject_report":
      if users_db.check_owner(admin.id) or users_db.check_dev(admin.id):
         try:
             await callback_query.edit_message_text(f"**Report Rejected By admin {admin.mention}!**")
         except Exception:
             await callback_query.delete()
   
