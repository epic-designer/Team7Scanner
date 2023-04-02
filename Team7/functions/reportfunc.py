from .check_reason import check_reason
from .basic import user_in_res
from .scanfunc import scancallpass

from Team7.core import Team7Scanner, assistant, user_errors, SCAN_LOGS 
from Team7.database import report_db, scan_db

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery

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

async def report_user_query(T7: Team7Scanner, message: Message):
   chat = message.chat
   user = message.from_user
   ask_user = await T7.ask(user.id, "Gime username or user id of user!", filters=filters.text)
   if await cancelled(ask_user):
      return
   try:
      report_user = await T7.get_users(ask_user.text)
      if await user_in_res(ask_user, report_user.id):
         return
      if report_db.check_report(report_user.id):
         await message.reply("user already in report list!")
         return
      if scan_db.check_scan(report_user.id):
         await message.reply("user already scanned by Team7")
         return
   except Exception as eror:
      if '[400 PEER_ID_INVALID]' in str(eror):
         await ask_user.repky("Forward any message of user and type /id replying that message! \nThen try again ✓")
         return
      error = user_errors(str(eror))
      await message.reply(str(error))
   ask_reason = await T7.ask(user.id, "Now Gime Reason code! Type /bancodes to get all reason codes!", filters.text)
   if await cancelled(ask_reason):
      return
   check_code, _ = check_reason(ask_reason.text)
   if check_code == "Null":
      await ask_reason.reply(f"Eh! `{ask_reason.text}` is wrong bancode! Type /bancodes to get all bancodes!")
      return
   reason_code = ask_reason.text
   ask_proof = await T7.ask(user.id, "Now Gime proof (single telegraph link)", filters.text)
   if await cancelled(ask_proof):
      return
   pr = ask_proof.text
   if pr.startswith("https://telegra.ph/file") or pr.startswith("https://telegra.ph") or pr.startswith("https://graph.org") or pr.startswith("https://graph.org/file"):
       proof = str(pr)
   else:
       await ask_proof.reply("need telegraph link as a proof!")
       return
   report_btn = [
                [ InlineKeyboardButton("• Scan/Accept •", callback_data=f"report_accept:{user.id}:{reason_code}:{proof}")
                ], [
                  InlineKeyboardButton("• Scan/Accept •", callback_data=f"report_reject")
                ],
                ]
   report_logs = "#REPORT! \n\n"
   report_logs += f"**By User:** {user.mention} (`{user.id}`) \n"
   report_logs += f"**To user:** {report_user.mention} (`{report_user.id}`) \n"
   report_logs += f"**Reason:** {check_code} \n"
   report_logs += f"**Proof:** `{proof}`"
   report_db.report_user(report_user.id, user.id)
   await T7.send_message(SCAN_LOGS, report_logs, reply_markup=InlineKeyboardMarkup(report_btn))
   await T7.send_message(user.id, f"User {report_user.mention} now in report list of Team7-scanner")


@Team7Scanner.on_callback_query(filters.regex(r'report_accept'))
async def scan_callback(T7: Team7Scanner, callback: CallbackQuery):
    query = callback.data.split(":")
    admin = callback.from_user
    message = callback.message
    if users_db.check_owner(admin.id) or users_db.check_dev(admin.id):
       user = await T7.get_users(query[0])
       reason = query[1]
       proof = query[2]
       await scancallpass(T7, callback, user, reason, proof)
    else:
       await callback.answer("Only Team7Scanne's Devs can!", show_alert=True) 
