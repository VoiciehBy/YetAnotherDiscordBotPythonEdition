import discord as d
import constants as c
import utils as u


class botClient(d.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def joinVoiceChannel(self, channel):
        voiceChannel = self.get_channel(channel.id)
        print(c.hiReply)
        if (not (voiceChannel)):
            return
        elif (not (self.voice_clients)):
            voiceClient = await voiceChannel.connect()

    async def on_ready(self):
        print(f"{botClient.user} has connected!11")
        if (c.autojoin):
            voiceChannel = u.getVoiceChannel(self)
            await self.joinVoiceChannel(voiceChannel)

    async def disconnect(self):
        print(c.byReply)
        if (self.voice_clients):
            await self.voice_clients[0].disconnect()
        await botClient.close()


async def sayHi(txtChannel):
    await txtChannel.send(c.hiReply)


async def playSong(voiceClient, song_name):
    song_path = u.download_music(u.music_url(song_name)).replace(
        '|', '_').replace(',', '_')  # fix

    if (voiceClient):
        if (not (voiceClient.is_playing()) and (voiceClient)):
            voiceClient.play(d.FFmpegPCMAudio(source=song_path))
            return 1
        else:
            print(c.playa_busy_txt)
            return -1


async def stopSong(voiceClient):
    if (voiceClient):
        voiceClient.stop()


async def printHelp(txtChannel):
    await txtChannel.send(u.commandsHelp())


async def purgeChannel(ch):
    await ch.purge()


async def sayThereIsNoSuchCommand(txtChannel):
    await txtChannel.send(c.defaultReply)
