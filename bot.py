import discord
from discord.ext import commands
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
        voiceChannel = botClient.get_channel(264064057038864386)
        voiceClient = await voiceChannel.connect()
        voiceClient.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe",source=r"music/song_name.mp3"))

botClient.run(constants.BOT_TOKEN)