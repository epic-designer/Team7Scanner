""" Team7 || RiZoeL """

from pyrogram import Client, filters
from pyrogram.types import Message
from Team7.database import report_db, users_db as db
from Team7.functions import report_user_query, getuser, user_in_res
from . import Owners, Devs


def sudo_checking(user_id):
   if db.check_owner(user_id):
      return True
   if db.check_dev(user_id):
      return True
   if db.check_sudo(user_id):
      return True 

@Client.on_message(filters.command(["report"], ["!", "/"]))
async def report_user_(T7: Client, message: Message):
    chat = message.chat
    user = message.from_user

    if user.id != chat.id:
       await message.reply("use this cmd in pm!")
       return

    if sudo_checking(user.id):
       await message.reply("You have rights to scan!")
       return

    await report_user_query(T7, message)

@Client.on_message(filters.user(Owners) & filters.command(["rmreport", "removereport"], ["!", "?", "/", "."]))
@Client.on_message(filters.user(Devs) & filters.command(["rmreport", "removereport"], ["!", "?", "/", "."]))
async def rmreport(T7: Client, message: Message):
   user = await getuser(T7, message)
   if await user_in_res(message, user.id):
      return

   if report_db.check_report(user.id):
      report_db.rm_report(user.id)
      await message.reply(f"{user.mention} removed from report list!")
   else:
      await message.reply("user not in report list!")
