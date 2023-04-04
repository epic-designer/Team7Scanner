
import re, io
from pyrogram import Client, filters
from pyrogram.types import Message
from . import Team7Users
from Team7.database import scan_db, report_db, users_db as db
from RiZoeLX.functions import delete_reply

Team7logo = "Team7/Team7Logo.jpg"

@Client.on_message(filters.user(Team7Users) & filters.command(["list"], ["!", "?", "/", "."]))
async def sevenlist(T7: Client, e: Message):
   hello = await e.reply_text("Processing...")
   txt = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
   if txt:
     See = txt[0]     
     if re.search("dev".lower(), See.lower()):
       data = db.get_all_devs()
       devs_ = "• All Current Devs Of Team7 \n\n"
       for usr in data:
          try:
             hm = await T7.get_users(int(usr.user_id))
             devs_ += f"  - {hm.first_name} ({hm.id}) \n"
          except:
             devs_ += f"  - {usr.user_id} \n"
       with io.BytesIO(str.encode(devs_)) as out_file:
             out_file.name = "Devlist.txt"
             await T7.send_document(
               chat_id=e.chat.id,
               document=out_file,
               thumb=Team7logo,
               caption="Dev list of Team7-scanner!",
               reply_to_message_id=e.id,
               )
             await hello.delete()

     elif re.search("sudo|redsudo".lower(), See.lower()):
       data = db.get_all_users()
       sudos_ = "• All Current sudos Of Team7\n\n"
       for usr in data:
          try:
             hm = await T7.get_users(int(usr.user_id))
             sudos_ += f"  - {hm.first_name} ({hm.id}), Bot: @{usr.username} \n"
          except:
             sudos_ += f"  - {usr.user_id}, Bot: @{usr.username} \n"
       with io.BytesIO(str.encode(sudos_)) as out_file:
             out_file.name = "Sudolist.txt"
             await T7.send_document(
               chat_id=e.chat.id,
               document=out_file,
               thumb=Team7logo,
               caption="Sudo list of Team7-scanner!",
               reply_to_message_id=e.id,
               )
             await hello.delete()

     elif re.search("bot".lower(), See.lower()):
       data = db.get_all_bots()
       bots_ = "**• All Current Bots added in Team7** \n\n" 
       for usr in data:
          bots_ += f"  - @{usr.username} ({usr.user_id}) \n"
       with io.BytesIO(str.encode(bots_)) as out_file:
             out_file.name = "Botlist.txt"
             await T7.send_document(
               chat_id=e.chat.id,
               document=out_file,
               thumb=Team7logo,
               caption="Bot list of Team7-scanner!",
               reply_to_message_id=e.id,
               )
             await hello.delete()

     else:
       await delete_reply(e, hello, "**Wrong Key!** \n\n __Keys:__ \n - `Devs` \n - `Sudos` \n - `Bots` ")
       return
   else:      
       await delete_reply(e, hello, "**wrong usage!** \n\n syntax: /list <key> \n\n __All Keys:__ \n - `Devs` \n - `Sudos` \n - `Bots` ")

           
@Client.on_message(filters.user(Team7Users) & filters.command(["scanlist"], ["!", "?", "/", "."]))
async def scanlist(T7: Client, e: Message):
   Hey = await e.reply("collecting....")
   data = scan_db.get_all_scanned()
   scanlist = "• All Current scanned users in Team7 \n\n"
   if len(data) > 0:
     for usr in data:
         try:
            hm = await T7.get_users(int(usr.user_id))
            scanlist += f"  - {hm.first_name} ({hm.id}), Reason: {usr.reason} \n"
         except:
            scanlist += f"  - {usr.user_id}, Reason: {usr.reason}\n"
     with io.BytesIO(str.encode(scanlist)) as out_file:
         out_file.name = "Scanlist.txt"
         await T7.send_document(
               chat_id=e.chat.id,
               document=out_file,
               thumb=Team7logo,
               caption="Scan users list of Team7-scanner!",
               reply_to_message_id=e.id,
               )
         await Hey.delete()
   else:
      await e.reply_text("No scan users (yet)")

          
@Client.on_message(filters.user(Team7Users) & filters.command(["reportlist"], ["!", "?", "/", "."]))
async def reportlist(T7: Client, e: Message):
   hey = await e.reply("collecting....")
   data = report_db.get_all_reports()
   reportlist = "• All Current scanned users in Red Seven \n\n"
   if len(data) > 0:
     for usr in data:
         reportlist += f"  - {usr.report_user_id}, reported by {usr.user_id} \n"
     with io.BytesIO(str.encode(reportlist)) as out_file:
         out_file.name = "Report list.txt"
         await T7.send_document(
               chat_id=e.chat.id,
               document=out_file,
               thumb=Team7logo,
               caption="Report users list of Red7-scanner!",
               reply_to_message_id=e.id,
               )
         await hey.delete()
   else:
      await e.reply_text("No report users (yet)")                    

