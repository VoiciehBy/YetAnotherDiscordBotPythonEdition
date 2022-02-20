import constants
import utils
import discord


async def sayHi(txtChannel):
    await txtChannel.send(constants.hiReply)


async def joinVoiceChannel(botClient, channel):
    voiceChannel = botClient.get_channel(channel.id)
    print(constants.hiReply)
    if(not(voiceChannel)):
        return
    elif(not(botClient.voice_clients)):
        voiceClient = await voiceChannel.connect()


async def disconnect(botClient):
    print(constants.byReply)
    if(botClient.voice_clients):
        await botClient.voice_clients[0].disconnect()
    await botClient.close()


async def playSong(voiceClient, song_name_with_ext):
    utils.download_music(utils.music_url(song_name_with_ext))
    if(voiceClient):
        voiceClient.play(discord.FFmpegPCMAudio(
            executable="ffmpeg.exe", source=constants.musicDirPath+song_name_with_ext))


async def stopSong(voiceClient):
    if(voiceClient):
        voiceClient.stop()


async def printHelp(txtChannel):
    await txtChannel.send(utils.commandsHelp())


async def sayThereIsNoSuchCommand(txtChannel):
    await txtChannel.send(constants.defaultReply)


async def purgeChannel(ch):
    await ch.purge()
