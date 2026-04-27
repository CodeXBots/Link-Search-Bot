import os
from typing import List

API_ID = os.environ.get("API_ID", "9282938")
API_HASH = os.environ.get("API_HASH", "9384849:39389")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", ""))
PICS = (os.environ.get("PICS", "")).split() # Add Multiple Images

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100xxxxxxxxx -100xxxxxxx").split()))  # Add Multiple channel id

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
