import discord
import botClient as bC
import utils as u
import constants as c

intents = discord.Intents.default()
intents.message_content = True
botClient = bC.botClient(intents=intents)


botClient.run(c.BOT_TOKEN)
