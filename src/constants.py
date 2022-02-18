import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TXT_CHANNEL_ID = int(os.getenv("BOT_TXT_CHANNEL_ID"))
BOT_VOICE_CHANNEL_ID = int(os.getenv("BOT_VOICE_CHANNEL_ID"))
cwd = os.getcwd()

PREFIX = '!'
hiReply = "Hehe,hihiho!!1"
byReply = "Cze,ja spadam,:D."
defaultReply = "Nie ma takiej komendy,XDddd."

commands = ["siema", "won", "połącz", "pomoc", "graj", "czyść"]
commands_desc = ["wyświetla " + "'" + hiReply + "'", "rozłącza bota", "podłącza bota do serwera głosowego",
                 "wyświetla pomoc", "odtwarza pewną pieśń", "czyści kanał tekstowy bota"]
