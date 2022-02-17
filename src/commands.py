import constants
import utils
import discord


async def sayHi(txtChannel):
    await txtChannel.send(constants.hiReply)


async def joinVoiceChannel(botClient, channel):
    voiceChannel = botClient.get_channel(channel.id)
    if(not(voiceChannel)):
        return
    else:
        voiceClient = await voiceChannel.connect()


async def disconnect(botClient):
    print(constants.byReply)
    await botClient.voice_clients[0].disconnect()


async def printHelp(txtChannel):
    await txtChannel.send(utils.commandsHelp())


async def playSong(voiceClient, song_name_with_ext):
    voiceClient.play(discord.FFmpegPCMAudio(
        executable="ffmpeg.exe", source=constants.cwd[:len(constants.cwd)-3] + r"music/"+song_name_with_ext))

async def sayThereIsNoSuchCommand(txtChannel):
    await txtChannel.send(constants.defaultReply)
