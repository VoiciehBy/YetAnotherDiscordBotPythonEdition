import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TXT_CHANNEL_ID = int(os.getenv("BOT_TXT_CHANNEL_ID"))