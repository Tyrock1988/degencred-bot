import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
BUSTER_USER_ID = int(os.getenv("BUSTER_USER_ID", "6668510825"))
CWALLET_BOT_USERNAME = os.getenv("CWALLET_BOT_USERNAME", "GambleCodezBank")
TRANSACTION_ALERT_THRESHOLD = float(os.getenv("TRANSACTION_ALERT_THRESHOLD", 1.00))
