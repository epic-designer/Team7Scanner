""" © Team7 || RiZoeL """

from database import users_db, scan_db
from core import assistant, SCAN_LOGS as seven_logs
from RiZoeLX.functions import delete_reply

scan_cmd = """
/revert {} 
Reason: {}
"""

async def scanpass(T7, message, user, reason):
   if user.username:
      bancmd = scan_cmd.format(user.username, reason)
   else:
      bancmd = scan_cmd.format(user.id, reason)

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

   final_text = f"User {user.mention} is Removed from Scanlist! \n\n cmd passed to `{done}` bots and failed in `{fail}` bots!")
   await delete_reply(message, huh, final_text)
   scan_db.scan_user(user.id, reason)
   log_msg = "**#REVERT** \n\n"
   log_msg += f"Admin: {message.from_user.mention}\n"
   log_msg += f"User: {user.mention} (`{user.id}`) \n"
   log_msg += f"Reason: `{reason}` \n"
   await T7.send_message(seven_logs, log_msg)
