""" © Team7 || RiZoeL """

from Team7.database import users_db, scan_db
from Team7.core.client import assistant
from Team7.core.config import SCAN_LOGS as seven_logs
from .redfunc import revert_to_red
from RiZoeLX.functions import delete_reply

scan_cmd = """
/revert {} 
"""

async def revertpass(T7, message, user):
   if user.username:
      bancmd = scan_cmd.format(user.username)
   else:
      bancmd = scan_cmd.format(user.id)

   huh = await message.reply("Passing cmd.....")
   done = 0
   fail = 0
   for bot in users_db.get_all_bots():
      try:
         await assistant.send_message(bot.username, bancmd)
         done += 1
      except:
         try:
            await assistant.send_message(bot.user_id, bancmd)
            done += 1
         except:
            fail += 1

   scan_db.revert_user(user.id)
   final_text = f"User {user.mention} is Removed from Scanlist! \n\n cmd passed to `{done}` bots and failed in `{fail}` bots!"
   await delete_reply(message, huh, final_text)
   try:
      await revert_to_red(user)
   except Exception as er:
      print(f"[Team7 INFO]: {str(er)}")
      pass
   log_msg = "**#REVERT** \n\n"
   log_msg += f"Admin: {message.from_user.mention}\n"
   log_msg += f"User: {user.mention} (`{user.id}`) "
   await T7.send_message(seven_logs, log_msg)


async def revertcallpass(T7, callback, user):
   if user.username:
      bancmd = scan_cmd.format(user.username)
   else:
      bancmd = scan_cmd.format(user.id)

   await callback.answer("passing cmd....")
   done = 0
   fail = 0
   for bot in users_db.get_all_bots():
      try:
         await assistant.send_message(bot.username, bancmd)
         done += 1
      except:
         try:
            await assistant.send_message(bot.user_id, bancmd)
            done += 1
         except:
            fail += 1
   try:
       await callback.edit_message_text(f"User {user.mention} is Removed from Scanlist! \n\n cmd passed to `{done}` bots and failed in `{fail}` bots!")
   except Exception:
       await callback.delete()
   try:
      await revert_to_red(user)
   except Exception as er:
      print(f"[Team7 INFO]: {str(er)}")
      pass
   scan_db.revert_user(user.id)
   log_msg = "**#REVERT** \n\n"
   log_msg += f"Admin: {callback.from_user.mention}\n"
   log_msg += f"User: {user.mention} (`{user.id}`) \n"
   await T7.send_message(seven_logs, log_msg)
