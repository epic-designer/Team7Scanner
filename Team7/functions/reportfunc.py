from Team7.database import report_db
from .check_reason import check_reason
from .basic import user_in_res
from Team7.core import Team7Scanner, assistant, user_errors, SCAN_LOGS 
from pyrogram import filters
from pyrogram.types import Message 

async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the Process!", quote=True)
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restarted the Bot!", quote=True)
        return True
    elif msg.text.startswith("/"):
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False

asyn def report_user_query(T7: Team7Scanner, message: Message):
   chat = message.chat
   user = message.from_user
   ask_user = await T7.ask(user.id, "Gime username or user id of user!", filters=filters.text)
   if await cancelled(ask_user):
      return
   try:
      report_user = await T7.get_users(ask_user.text)
      if await user_in_res(ask_user, report_user.id)
         return
   except Exception as eror:
      if '[400 PEER_ID_INVALID]' in str(eror):
         await ask_user.repky("Forward any message of user and type /id replying that message! \nThen try again ✓")
         return
      error = user_errors(str(eror))
      await message.reply(str(error))
   ask_reason = await T7.ask(user.id, "Now Gime Reason code! Type /bancodes to get all reason codes!", filters.text)
   check_code, _ = await check_reason(ask_reason.text)
   if check_code == "Null":
      await ask_reason.reply(f"Eh! `{ask_reason.text}` is wrong bancode! Type /bancodes to get all bancodes!")
      return
   reason_code = ask_reason.text
   ask_proof = await T7.ask(user.id, "Now Gime proof (single telegraph link)", filters.text)
   pr = ask_proof.text
   if pr.startswith("https://telegra.ph/file") or pr.startswith("https://telegra.ph") or pr.startswith("https://graph.org") or pr.startswith("https://graph.org/file"):
       proof = str(pr)
   else:
       await ask_proof.reply("need telegraph link as a proof!")
       return
   report_btn = [
                [ InlineKeyboardButton("• Scan/Accept •", callback_data=f"report_accept:{user.id}:{reason_code}:{proof}")
                ], [
                  InlineKeyboardButton("• Scan/Accept •", callback_data=f"report_reject:{user.id}:{reason_code}:{proof}")
                ],
                ]
   report_logs = "#REPORT! \n\n"
   report_logs += f"**By User:** {user.mention} (`{user.id}`) \n"
   report_logs += f"**To user:** {report_user.mention} (`report_user.id}`) \n"
   report_logs += f"**Reason:** {check_code} \n"
   report_logs += f"**Proof:** `{proof}`"
   await T7.send_message(SCAN_LOGS, report_logs, reply_markup=InlineKeyboardMarkup(report_btn))
   await T7.send_message(user.id, f"User {report_user.mention} now in report list of Team7-scanner")
   
