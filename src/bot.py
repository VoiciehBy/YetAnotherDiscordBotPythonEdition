import discord
import commands
import utils as u
import constants as c

intents = discord.Intents.default()
intents.message_content = True
botClient = commands.botClient(intents=intents)


botClient.run(c.BOT_TOKEN)
