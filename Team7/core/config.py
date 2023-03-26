import os
from dotenv import load_dotenv
from Team7.functions import make_list

if os.path.exists(".env"):
    load_dotenv(".env")


" ===================== CONFIGS ===================== "

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
TOKEN = int(os.getenv("TOKEN", ""))
SESSION = os.getenv("SESSION", "")
OWNER_IDS = make_list(os.getenv("OWNER_IDS", ""))
DEVS = make_list(os.getenv("DEVS", ""))
SUDO_USERS = make_list(os.getenv("SUDO_USERS", ""))
SCAN_LOGS = os.getenv("SCAN_LOGS", "")
SEVEN_LOGS = os.getenv("SEVEN_LOGS", "")
