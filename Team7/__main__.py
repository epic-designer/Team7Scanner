
import os, sys
from Team7.core import *
from Team7.database import users_db

print("[Team7 INFO]: Adding users in db!")
for user_id in OWNER_IDS:
   user_db.add_owner(user_id)

print("[Team7 INFO]: Adding Devs in DB")
for user_id in DEVS:
   user_db.add_dev(user_id)
print("[Team7 INFO]: Added all devs in DB")
print("[Team7 INFO]: Moving to next steps!")

if __name__ == "__main__":
   Start_assistant()
   StartScanner()


