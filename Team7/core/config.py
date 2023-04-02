import os, sys
from dotenv import load_dotenv
from Team7.functions import make_list

if os.path.exists(".env"):
    load_dotenv(".env")


" ===================== CONFIGS ===================== "

API_ID = int(os.getenv("API_ID", ""))
if not API_ID:
   print("[Team7 INFO]: You didn't fill API_ID var!")
   sys.exit()
else:
   print("[Team7 INFO]: Got API_ID")

API_HASH = os.getenv("API_HASH", "")
if not API_HASH:
   print("[Team7 INFO]: You didn't fill API_HASH var!")
   sys.exit()
else:
   print("[Team7 INFO]: Got API_HASH")

TOKEN = int(os.getenv("TOKEN", ""))
if not TOKEN:
   print("[Team7 INFO]: You didn't fill TOKEN var!")
   sys.exit()
else:
   print("[Team7 INFO]: Got TOKEN")

SESSION = os.getenv("SESSION", "")
if not SESSION:
   print("[Team7 INFO]: You didn't fill SESSION var!")
   sys.exit()
else:
   print("[Team7 INFO]: Got SESSION")

OWNER_IDS = make_list(os.getenv("OWNER_IDS", ""))
if not OWNER_IDS:
   print("[Team7 INFO]: You didn't fill OWNER_IDS var!")
   sys.exit()
else:
   print("[Team7 INFO]: Got OWNER_IDS")

DEVS = make_list(os.getenv("DEVS", ""))
SCAN_LOGS = os.getenv("SCAN_LOGS", "")
SEVEN_LOGS = os.getenv("SEVEN_LOGS", "")
