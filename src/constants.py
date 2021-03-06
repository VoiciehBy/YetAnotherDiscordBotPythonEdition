import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_TXT_CHANNEL_ID = int(os.getenv("BOT_TXT_CHANNEL_ID"))
BOT_VOICE_CHANNEL_ID = int(os.getenv("BOT_VOICE_CHANNEL_ID"))
cwd = os.getcwd()
musicDirPath = cwd[:len(cwd)-3] + "\\" + r"music" + "\\"
ytUrl = "https://www.youtube.com/"
default_music_download_extension = "m4a"
autojoin = True

PREFIX = '!'
hiReply = "Hehe,hihiho!!1"
byReply = "Cze,ja spadam,:D."
defaultReply = "Nie ma takiej komendy,XDddd."

commands = ["siema", "połącz", "won", "graj", "stop", "czyść",  "pomoc"]
commands_desc = ["wyświetla " + "'" + hiReply + "'", "podłącza bota do serwera głosowego", "rozłącza bota",
                 "odtwarza pewną pieśń", "zatrzymuje muzykę", "czyści kanał tekstowy bota", "wyświetla pomoc"]

now_txt = "Teraz: "
next_txt = "Za chwilę: "
playa_busy_txt = "The playa busy..."