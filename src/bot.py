import discord
import commands
import utils
import constants

botClient = discord.Client()


@botClient.event
async def on_ready():
    print(f"{botClient.user} has connected!11")
    if(constants.autojoin):
        voiceChannel = utils.getVoiceChannel(botClient)
        await commands.joinVoiceChannel(botClient, voiceChannel)


@botClient.event
async def handleCommands(msg):
    if (utils.isCommmand(msg)):
        cmd_name = utils.getCommandName(msg)
        cmd_arg = utils.getCommandArguments(msg)
        if (cmd_name == constants.commands[0]):
            await commands.sayHi(msg.channel)
        elif (cmd_name == constants.commands[1]):
            voiceChannel = utils.getVoiceChannel(botClient)
            await commands.joinVoiceChannel(botClient, voiceChannel)
        elif (cmd_name == constants.commands[2]):
            await commands.disconnect(botClient)
        elif (cmd_name == constants.commands[3]):
            await msg.channel.send(constants.next_txt + utils.song_title(utils.music_url(cmd_arg)))
            await commands.playSong(botClient.voice_clients[0], cmd_arg)
            await msg.channel.send(constants.now_txt + utils.song_title(utils.music_url(cmd_arg)))
        elif (cmd_name == constants.commands[4]):
            await commands.stopSong(botClient.voice_clients[0])
        elif (cmd_name == constants.commands[5]):
            await commands.purgeChannel(msg.channel)
        elif (cmd_name == constants.commands[6]):
            await commands.printHelp(msg.channel)
        else:
            await commands.sayThereIsNoSuchCommand(msg.channel)


@botClient.event
async def on_message(msg):
    if(not(utils.ifMsgOnTheChannel(msg, constants.BOT_TXT_CHANNEL_ID)) or utils.ifMsgComesFromBot(msg)):
        return
    else:
        await handleCommands(msg)

botClient.run(constants.BOT_TOKEN)
