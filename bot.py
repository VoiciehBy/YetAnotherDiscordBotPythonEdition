import os
import discord
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

botClient = discord.Client()


@botClient.event
async def on_ready():
    print(f"{botClient.user} has connected!11")

botClient.run(BOT_TOKEN)