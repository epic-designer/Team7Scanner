from .check_reason import check_reason
from .basic import user_in_res, make_tg, tg_download
from .scanfunc import scancallpass

from Team7.core import Team7Scanner, assistant, user_errors, SCAN_LOGS 
from Team7.database import report_db, scan_db, users_db

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyroaddon import listen

async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the Process!", quote=True)
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restarted!", quote=True)
        return True
    elif msg.text.startswith("/"):
        await msg.reply("Cancelled the process!", quote=True)
        return True
    else:
        return False

async def report_user_query(T7: Team7Scanner, message: Message):
   chat = message.chat
   ask_user = await T7.ask(chat.id, "Gime username or user id of user!", filters=filters.text, timeout=300)
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
      if report_user.id == chat.id:
         await message.reply("🧐 You want to report your self ?")
         return
   except Exception as eror:
      if '[400 PEER_ID_INVALID]' in str(eror):
         await ask_user.reply("Forward any message of user and type /id replying that message! \nThen try again ✓")
         return
      error = user_errors(str(eror))
      await message.reply(str(error))
      return
   ask_reason = await T7.ask(chat.id, "Now Gime Reason code! Type /bancodes to get all reason codes!", filters.text, timeout=300)
   if await cancelled(ask_reason):
      return
   check_code, _ = check_reason(ask_reason.text)
   if check_code == "Null":
      await ask_reason.reply(f"Eh! `{ask_reason.text}` is wrong bancode! Type /bancodes to get all bancodes!")
      return
   reason_code = ask_reason.text
   ask_proof = await T7.ask(chat.id, "Now Gime proof (single telegraph link) or photo", timeout=300)
   if ask_proof.photo:
      proof = await make_tg(ask_proof)
   elif ask_proof.text:
      if await cancelled(ask_proof):
         return
      pr = ask_proof.text
      if pr.startswith("https://telegra.ph/file") or pr.startswith("https://telegra.ph") or pr.startswith("https://graph.org") or pr.startswith("https://graph.org/file"):
         proof = str(pr)
      else:
         await ask_proof.reply("need telegraph link as a proof!")
         return
   else:
       await ask_proof.reply("send Telegraph link or photo!")
       return
   msg = await T7.send_message("T7PROOF", proof)
   report_btn = [
                [ InlineKeyboardButton("• Scan/Accept •", callback_data=f"report:{report_user.id}:{reason_code}:{msg.id}")
                ], [
                  InlineKeyboardButton("• Reject Report •", callback_data=f"report:reject:{report_user.id}")
                ],
                ]
   report_logs = "#REPORT! \n\n"
   report_logs += f"**By User:** {message.from_user.mention} (`{message.from_user.id}`) \n"
   report_logs += f"**To user:** {report_user.mention} (`{report_user.id}`) \n"
   report_logs += f"**Reason:** {check_code} \n"
   report_logs += f"**Proof:** `{proof}`"
   report_db.report_user(report_user.id, chat.id)
   await T7.send_message(SCAN_LOGS, report_logs, reply_markup=InlineKeyboardMarkup(report_btn))
   await T7.send_message(chat.id, f"User {report_user.mention} now in report list of Team7-scanner")


@Team7Scanner.on_callback_query(filters.regex(r'report'))
async def scan_callback(T7: Team7Scanner, callback: CallbackQuery):
    query = callback.data.split(":")
    admin = callback.from_user
    message = callback.message
    if users_db.check_owner(admin.id) or users_db.check_dev(admin.id):
       if query[1] == "reject":
          user_id = query[2]
          report_db.rm_report(user_id)
          try:
             await callback.edit_message_text(f"**Report Rejected By admin {admin.mention}!**")
          except Exception:
             await callback.delete()
          return
       else:
          user_id = int(query[1])
          user = await T7.get_users(user_id)
          reason = query[2]
          msg = await T7.get_messages("T7PROOF", int(query[3]))
          proof = str(msg.text)
          await scancallpass(T7, callback, user, reason, proof)
    else:
       await callback.answer("Only Team7Scanne's Devs can!", show_alert=True) 
