from Team7.database import users_db 
from Team7.core.client import Team7Scanner


async def itsme(message, user_id):
    me = await Team7Scanner.get_me()
    if user_id == me.id:
       await message.reply("Noob 😑 It's mee!")
       return True

async def user_in_owners(message, user_id):
   if users_db.check_owner(user_id):
       await message.reply("User is an owner!")
       return True
   
async def user_in_sudos(message, user_id):
   if users_db.check_sudo(user_id):
       await message.reply("User in Sudo List!")
       return True 

async def user_in_devs(message, user_id):
   if users_db.check_dev(user_id):
       await message.reply("User in Dev List!")
       return True

async def user_in_res(message, user_id):
   if user_in_owners(message, user_id):
       return True
   if user_in_devs(message, user_id):
       return True
   if user_in_sudos(message, user_id):
       return True
   if itsme(message, user_id):
       return True

async def owner_dev(message, user_id):
   if user_in_owners(message, user_id):
       return True 
   if user_in_devs(message, user_id):
       return True 
