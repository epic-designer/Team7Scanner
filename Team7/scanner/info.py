""" Team7 || RiZoeL """

from Team7.database import users_db, scan_db, report_db
from pyrogram import filters, Client
from pyrogram.types import Message
from . import Owners
import asyncio 

async def itt7(T7, message, user):
   me = await T7.get_me()
   if user.id == me.id:
      Msg = "**It's me! Team7's Scanner!** \n\n"
      Msg += "  • I'm An advance and fast pyrogram based scanner! \n" 
      await message.reply(Msg)
      return True 

@Client.on_message(filters.command(["info", "tinfo"], ["!", "?", "/", "."]))
async def seven_info(T7: Client, e: Message):
   """ Info only owner, devs & bot owners can """
   txt = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
   if e.reply_to_message:
      try:
         user = await T7.get_users(e.reply_to_message.from_user.id)
      except:
         try:
            user = e.reply_to_message.from_user
         except Exception as eor:
            await e.reply(str(eor))
            return
   elif txt:
      try:
         user = await T7.get_users(txt[0])
      except Exception as eor:
         await e.reply(str(eor))
         return
   else:
      try:
         user = await T7.get_users(e.from_user.id)
      except:
         try:
            user = e.from_user
         except Exception as eor:
            await e.reply(str(eor))
            return

   if await itt7(T7, e, user):
      return 

   msg = "**User INFO!** \n\n"
   msg += "===================\n"
   msg += f"**First Name:** {user.first_name} \n"
   if user.last_name:
      msg += f"**Last Name:** {user.last_name} \n"
   msg += f"**User ID:** `{user.id}` \n"
   if user.username:
      msg += f"**Username:** @{user.username} \n"
   msg += f"**User link** [link](tg://user?id={user.id}) \n"
   if users_db.check_owner(int(user.id)):
      msg += "**Rank:** Owner 🔱 \n"
   if users_db.check_dev(int(user.id)):
      msg += "**Rank:** Dev ⚜️ \n"
   if users_db.check_user(int(user.id)):
      msg += "**Rank:** 7-Sudo 👤 \n"
   if scan_db.check_scan(int(user.id)):
      msg += "**Scanned user: Yes!** \n"
   if report_db.check_report(user.id):
      msg += "**User in Report list!** \n"
   msg += "==================="
   await e.reply_text(msg)


@Client.on_message(filters.command(["t7info", "seveninfo"], ["!", "?", "/", "."]))
async def team7_info(T7: Client, message: Message):
   hui = await message.reply("!-----")
   await asyncio.sleep(0.4)
   await hui.edit_text("-!----")
   await asyncio.sleep(0.4)
   await hui.edit_text("--!---")
   await asyncio.sleep(0.4)
   await hui.edit_text("---!--")
   await asyncio.sleep(0.4)
   await hui.edit_text("----!-")
   await asyncio.sleep(0.4)
   await hui.edit_text("-----!")
   await asyncio.sleep(0.4)
   await hui.edit_text("-!----")
   await asyncio.sleep(0.4)
   await hui.edit_text("--!---")
   await asyncio.sleep(0.4)
   await hui.edit_text("---!--")
   await asyncio.sleep(0.4)
   await hui.edit_text("----!-")
   await asyncio.sleep(0.4)
   await hui.edit_text("-----!")
   await asyncio.sleep(0.4)
   await hui.edit_text("checking in database----")
   await asyncio.sleep(0.6)
   await hui.edit_text("Gotcha 😉")
   await asyncio.sleep(0.6)
   await hui.edit_text("😈")
   await asyncio.sleep(1)
   await hui.edit_text("Heyyy master!!")
   await asyncio.sleep(1)
   await hui.delete()
   msg = f"**Here is my {message.from_user.mention} Sweet and sanki Owner!** 😉"
   vid = "https://telegra.ph/file/424e60342e214bf267552.mp4"
   await message.reply_video(vid, caption=msg)
   
   
   
   
