from Team7.database import users_db 

async def user_in_owners(message, user_id):
   if users_db.check_owner(user_id):
       await message.reply("User is an owner!")
       return
   
async def user_in_sudos(message, user_id):
   if users_db.check_sudo(user_id):
       await message.reply("User in Sudo List!")
       return

async def user_in_devs(message, user_id):
   if users_db.check_dev(user_id):
       await message.reply("User in Dev List!")
       return

async def user_in_res(message, user_id):
   if users_db.check_owner(user_id):
       await message.reply("User is an owner!")
       return
   if users_db.check_dev(user_id):
       await message.reply("User in Dev List!")
       return
   if users_db.check_sudo(user_id):
       await message.reply("User in Sudo List!")
       return

