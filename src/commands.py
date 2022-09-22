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

    async def disconnect(self):
        print(c.byReply)
        if (self.voice_clients):
            await self.voice_clients[0].disconnect()
        await self.close()

    async def playSong(self, voiceClient, song_name):
        song_path = u.download_music(u.music_url(song_name)).replace(
            '|', '_').replace(',', '_')  # fix

        if (voiceClient):
            if (not (voiceClient.is_playing())):
                voiceClient.play(d.FFmpegPCMAudio(source=song_path))
                return 1
            else:
                print(c.playa_busy_txt)
                return -1

    async def stopSong(self, voiceClient):
        if (voiceClient):
            voiceClient.stop()

    async def sendMessage(self, txtChannel, txt):
        await txtChannel.send(txt)

    async def sayHi(self, txtChannel):
        await self.sendMessage(txtChannel, c.hiReply)

    async def sayBye(self, txtChannel):
        await self.sendMessage(txtChannel, c.byReply)

    async def purgeChannel(self, ch):
        await ch.purge()

    async def printHelp(self, txtChannel):
        await txtChannel.send(u.commandsHelp())

    async def sayThereIsNoSuchCommand(self, txtChannel):
        await self.sendMessage(txtChannel, c.defaultReply)

    async def on_ready(self):
        print(f"{self.user} has connected!11")
        if (c.autojoin):
            voiceChannel = u.getVoiceChannel(self)
            await self.joinVoiceChannel(voiceChannel)

    async def handleCommands(self, msg):
        if (u.isCommmand(msg)):
            cmd_name = u.getCommandName(msg)
            cmd_arg = u.getCommandArguments(msg)
            if (cmd_name == c.commands[0]):
                await self.sayHi(msg.channel)
            elif (cmd_name == c.commands[1]):
                voiceChannel = u.getVoiceChannel(self)
                await self.joinVoiceChannel(voiceChannel)
            elif (cmd_name == c.commands[2]):
                await self.sayBye(msg.channel)
                await self.disconnect()
            elif (cmd_name == c.commands[3]):
                song_title = u.song_title(u.music_url(cmd_arg))
                await self.sendMessage(msg.channel, c.next_txt + song_title)
                if (await self.playSong(self.voice_clients[0], cmd_arg) == 1):
                    await self.sendMessage(msg.channel, c.now_txt + song_title)
                elif (await self.playSong(self.voice_clients[0], cmd_arg) == -1):
                    await self.sendMessage(msg.channel, c.playa_busy_txt)
            elif (cmd_name == c.commands[4]):
                await self.stopSong(self.voice_clients[0])
            elif (cmd_name == c.commands[5]):
                await self.purgeChannel(msg.channel)
            elif (cmd_name == c.commands[6]):
                await self.printHelp(msg.channel)
            else:
                await self.sayThereIsNoSuchCommand(msg.channel)

    async def on_message(self, msg):
        if (not (u.ifMsgOnTheChannel(msg, c.BOT_TXT_CHANNEL_ID)) or u.ifMsgComesFromBot(msg)):
            return
        else:
            await self.handleCommands(msg)
