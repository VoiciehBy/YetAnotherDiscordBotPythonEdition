import constants
import utils
import discord


async def sayHi(txtChannel):
    await txtChannel.send(constants.hiReply)


async def disconnect(botClient):
    print(constants.byReply)
    if(botClient.voice_clients):
        await botClient.voice_clients[0].disconnect()
    await botClient.close()


async def joinVoiceChannel(botClient, channel):
    voiceChannel = botClient.get_channel(channel.id)
    print(constants.hiReply)
    if(not(voiceChannel)):
        return
    elif(not(botClient.voice_clients)):
        voiceClient = await voiceChannel.connect()


async def playSong(voiceClient, song_name_with_ext):
    if(voiceClient):
        voiceClient.play(discord.FFmpegPCMAudio(
            executable="ffmpeg.exe", source=constants.cwd[:len(constants.cwd)-3] + r"music/"+song_name_with_ext))


async def printHelp(txtChannel):
    await txtChannel.send(utils.commandsHelp())


async def sayThereIsNoSuchCommand(txtChannel):
    await txtChannel.send(constants.defaultReply)


async def purgeChannel(ch):
    await ch.purge()
