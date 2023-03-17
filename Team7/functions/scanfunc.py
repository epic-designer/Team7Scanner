""" © Team7 || RiZoeL """

from database import users_db
from core import assistant, seven_logs
from RiZoeLX.functions import delete_reply

scan_cmd = """
/gban {} 
Reason: {}
Proof: {}

Note: user {} is official scanned by Team7 || Red7
"""

async def scanpass(T7, message, user, reason, proof):
   if user.username:
      bancmd = scan_cmd.format(user.username, reason, proof, user.first_name)
   else:
      bancmd = scan_cmd.format(user.id, reason, proof, user.first_name)

   huh = await message.reply("Passing cmd..")
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

   final_text = f"User {user.mention} in scan list! \n\n cmd passed to `{done}` bots and failed in `{fail}` bots!")
   await delete_reply(message, huh, final_text)
   log_msg = "**#SCAN** \n\n"
   log_msg += f"Admin: {message.from_user.mention}\n"
   log_msg += f"User: {user.mention} (`{user.id}`) \n"
   log_msg += f"Reason: `{reason}` \n"
   log_msg += f"Proof: `{proof}` \n"
   await T7.send_message(seven_logs, log_msg)
   try:
      to_user_text = f"Hey {user.mention}! \n\n You're Scanned By [Team7](https://t.me/Team7_Support_chats) \n\n Reason: {reason} \n Proof: {proof}"
      if user.username:
         await assistant.send_message(user.username, to_user_text, disable_web_page_preview=True)
      else:
         await assistant.send_message(user.id, to_user_text, disable_web_page_preview=True)
   except:
      print(f"{user.first_name} is Noob!")
      pass
