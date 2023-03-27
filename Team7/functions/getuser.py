""" © Team7 || RiZoeL """

from functions.check_reason import *
from database import users_db as db

def import_owners():
   Owners = []
   for x in db.get_all_owners():
      Owners.append(x.user_id)
   return Owners

def import_devs():
   Devs = []
   for x in db.get_all_devs():
      Devs.append(x.user_id)
   return Devs

def import_sudos():
   Sudos = []
   for x in db.get_all_sudos():
      Owners.append(x.user_id)
   return Sudos

def import_members():
   own = import_owners()
   sud = import_sudos()
   dev = import_devs()
   Members = own + sud + dev
   return Members

"""Members = []
   for x in db.get_all_owners():
      Members.append(x.user_id)
   for x in db.get_all_devs():
      Members.append(x.user_id)
   for x in db.get_all_sudos():
      Members.append(x.user_id)
   return Members"""

async def get_urp(T7, message):
   args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
   txt = args[1:]
   if len(txt) == 2:
      try:
         user = await T7.get_users(args[0])
      except Exception as error:
         await message.reply(f"Error! {error}")
         return
      reason = txt[0]
      proof = str(txt[1])
      return user, reason, proof

   elif message.reply_to_message:
      try:
         user = await T7.get_users(message.reply_to_message.from_user.id)
      except:
         try:
            user = message.reply_to_message.from_user
         except Exception as error:
            await message.reply(f"Error! {error}")
            return
      reason = str(args[0])
      proof = str(args[1])
      return user, reason, proof

   else:
      await message.reply("**Wrong Usage:** Syntax: .scan (user) (ban code only) (single telegraph file/proof link)")

async def getuser(T7, message):
   args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
   if message.reply_to_message:
      try:
         user = await T7.get_users(message.reply_to_message.from_user.id)
      except:
         try:
            user = message.reply_to_message.from_user
         except Exception as error:
            await message.reply(f"Error! {error}")
            return
   elif args:
      try:
         user = await T7.get_users(args[0])
      except Exception as error:
         await message.reply(f"Error! {error}")
         return

   else:
      await message.reply("**Wrong Usage:** Syntax: .scan (user) (ban code only) (single telegraph file/proof link)")

async def getuser_extra(T7, message):
   args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)

   if message.reply_to_message:
      try:
         user = await T7.get_users(message.reply_to_message.from_user.id)
      except:
         try:
            user = message.reply_to_message.from_user
         except Exception as error:
            await message.reply(f"Error! {error}")
            return
      try
         extra = await T7.get_users(args[0])
      except Exception as er:
         await message.reply(f"Error! {er}")
         return
      return user, extra

   if len(args) == 2:
      try:
         user = await T7.get_users(args[0])
      except Exception as error:
         await message.reply(f"Error! {error}")
         return
      try
         extra = await T7.get_users(args[1])
      except Exception as er:
         await message.reply(f"Error! {er}")
         return
      return user, extra

   else:
      await message.reply("Error! This cmd need 2 values")
