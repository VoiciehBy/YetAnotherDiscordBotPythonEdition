import discord
import utils
import constants

botClient = discord.Client()


@botClient.event
async def on_ready():
    print(f"{botClient.user} has connected!11")


@botClient.event
async def on_message(msg):
    ch = msg.channel
    if(ch.id != constants.BOT_TXT_CHANNEL_ID or msg.author == botClient.user):
        return
    else:
        botMsg = await ch.send(msg.content)
        await botMsg.delete()
        await utils.purgeChannel(ch)

botClient.run(constants.BOT_TOKEN)