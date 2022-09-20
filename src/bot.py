import discord
import commands
import utils as u
import constants as c

intents = discord.Intents.default()
intents.message_content = True
botClient = commands.botClient(intents=intents)

@botClient.event
async def handleCommands(msg):
    if (u.isCommmand(msg)):
        cmd_name = u.getCommandName(msg)
        cmd_arg = u.getCommandArguments(msg)
        if (cmd_name == c.commands[0]):
            await commands.sayHi(msg.channel)
        elif (cmd_name == c.commands[1]):
            voiceChannel = u.getVoiceChannel(botClient)
            await botClient.joinVoiceChannel(voiceChannel)
        elif (cmd_name == c.commands[2]):
            await msg.channel.send(c.byReply)
            await botClient.disconnect()
        elif (cmd_name == c.commands[3]):
            await msg.channel.send(c.next_txt + u.song_title(u.music_url(cmd_arg)))
            if(await commands.playSong(botClient.voice_clients[0], cmd_arg) == 1):
                await msg.channel.send(c.now_txt + u.song_title(u.music_url(cmd_arg)))
            elif(await commands.playSong(botClient.voice_clients[0], cmd_arg) == -1):
                await msg.channel.send(c.playa_busy_txt)
        elif (cmd_name == c.commands[4]):
            await commands.stopSong(botClient.voice_clients[0])
        elif (cmd_name == c.commands[5]):
            await commands.purgeChannel(msg.channel)
        elif (cmd_name == c.commands[6]):
            await commands.printHelp(msg.channel)
        else:
            await commands.sayThereIsNoSuchCommand(msg.channel)


@botClient.event
async def on_message(msg):
    if(not(u.ifMsgOnTheChannel(msg, c.BOT_TXT_CHANNEL_ID)) or u.ifMsgComesFromBot(msg)):
        return
    else:
        await handleCommands(msg)

botClient.run(c.BOT_TOKEN)
