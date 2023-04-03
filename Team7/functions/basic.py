import os
from Team7.database import users_db 
from Team7.core.client import Team7Scanner
from pyrogram.types import Message 
from telegraph import Telegraph, exceptions, upload_file


async def itsme(message: Message, user_id):
    me = await Team7Scanner.get_me()
    if user_id == me.id:
       await message.reply("Noob 😑 It's mee!")
       return True

async def user_in_owners(message: Message, user_id):
   if users_db.check_owner(user_id):
       await message.reply("User is an owner!")
       return True
   
async def user_in_sudos(message: Message, user_id):
   if users_db.check_sudo(user_id):
       await message.reply("User in Sudo List!")
       return True 

async def user_in_devs(message: Message, user_id):
   if users_db.check_dev(user_id):
       await message.reply("User in Dev List!")
       return True

async def user_in_res(message: Message, user_id):
   if await user_in_owners(message, user_id):
       return True
   if await user_in_devs(message, user_id):
       return True
   if await user_in_sudos(message, user_id):
       return True
   if await itsme(message, user_id):
       return True

async def owner_dev(message: Message, user_id):
   if await user_in_owners(message, user_id):
       return True 
   if await user_in_devs(message, user_id):
       return True 

async def make_tg(message):
   tx = await message.reply("downloading media...")
   doc = await message.download()
   try:
      media_url = upload_file(doc)
      tg_url = f"https://telegra.ph/{media_url[0]}"
      os.remove(doc)
      await tx.delete()
      return tg_url
   except exceptions.TelegraphException as exc:
      await message.reply(f"**ERROR:** `{exc}`")
      os.remove(doc)
      return 

async def tg_download(message):
   doc = await message.download()
   try:
      media_url = upload_file(doc)
      tg_url = f"https://telegra.ph/{media_url[0]}"
      os.remove(doc)
      return tg_url
   except exceptions.TelegraphException as exc:
      os.remove(doc)
      return
