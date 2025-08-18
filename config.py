from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
TZ = os.getenv("TZ", "Asia/Almaty")
MY_CHAT_ID = 123456789