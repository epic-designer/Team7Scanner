""" © Team7 || RiZoeL """

from functions.check_reason import *

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
   args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
   txt = args[1:]
   if len(txt) == 2:
      try:
         user = await T7.get_users(args[0])
      except Exception as error:
         await message.reply(f"Error! {error}")
         return

   elif message.reply_to_message:
      try:
         user = await T7.get_users(message.reply_to_message.from_user.id)
      except:
         try:
            user = message.reply_to_message.from_user
         except Exception as error:
            await message.reply(f"Error! {error}")
            return

   else:
      await message.reply("**Wrong Usage:** Syntax: .scan (user) (ban code only) (single telegraph file/proof link)")
