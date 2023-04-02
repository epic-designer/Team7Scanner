
import os, sys, asyncio
from Team7.core import OWNER_IDS, DEVS, StartScanner
from Team7.database import users_db

print("[Team7 INFO]: Adding users in db!")
for user_id in OWNER_IDS:
   users_db.add_owner(user_id)

print("[Team7 INFO]: Adding Devs in DB")
for user_id in DEVS:
   users_db.add_dev(user_id)
print("[Team7 INFO]: Added all devs in DB")
print("[Team7 INFO]: Moving to next steps!")

if __name__ == "__main__":
  asyncio.run(await StartScanner())


