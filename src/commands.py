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


async def playSong(voiceClient, song_name):
    song_path = utils.download_music(utils.music_url(song_name)).replace('|', '_')#fix

    if(voiceClient):
        if(not(voiceClient.is_playing()) and (voiceClient)):
            voiceClient.play(discord.FFmpegPCMAudio(source=song_path))
            return 1
        else:
            print(constants.playa_busy_txt)
            return -1


async def stopSong(voiceClient):
    if(voiceClient):
        voiceClient.stop()


async def printHelp(txtChannel):
    await txtChannel.send(utils.commandsHelp())


async def purgeChannel(ch):
    await ch.purge()


async def sayThereIsNoSuchCommand(txtChannel):
    await txtChannel.send(constants.defaultReply)
