""" © Team7 RiZoeL """
import time, datetime

from Team7.database import users_db
from Team7.funtions import report_user_query, get_time
from Team7.core import alive_msg, get_stats

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_callback_query()
async def T7callbacks(T7: Client, callback_query: CallbackQuery):
   query = callback_query.data.lower()
   chat = callback_query.message.chat
   admin = callback_query.from_user
   message = callback_query.message
   if query == "do_report":
      await report_user_query(T7, message)

   elif query == "reject_report":
      if users_db.check_owner(admin.id) or users_db.check_dev(admin.id):
         try:
             await callback_query.edit_message_text(f"**Report Rejected By admin {admin.mention}!**")
         except Exception:
             await callback_query.delete()
      else:
         await callback_query.answer("Only Team7's devs can!", show_alert=True)

   elif query == "ping":
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await callback_query.answer(f"**Team7 Scanner Here!** \n\n Ping: {ms}ms \n Uptime: {uptime}", show_alert=True)

   elif query == "alive":
      await callback_query.answer(alive_msg, show_alert=True)

   elif query == "stats":
      await callback_query.answer(get_stats(), show_alert=True)

   

