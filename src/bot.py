import discord
import commands
import utils
import constants

botClient = discord.Client()


@botClient.event
async def on_ready():
    print(f"{botClient.user} has connected!11")


@botClient.event
async def handleCommands(msg):
    if (utils.isCommmand(msg)):
        cmd_name = utils.getCommandName(msg)
        if (cmd_name == constants.commands[0]):
            await commands.sayHi(msg.channel)
        elif (cmd_name == constants.commands[1]):
            await commands.disconnect(botClient)
        elif (cmd_name == constants.commands[2]):
            voiceChannel = utils.getVoiceChannel(botClient)
            await commands.joinVoiceChannel(botClient, voiceChannel)
        elif (cmd_name == constants.commands[3]):
            await commands.printHelp(msg.channel)
        elif (cmd_name == constants.commands[4]):
            await commands.playSong(botClient.voice_clients[0], "song_name.format")
        elif (cmd_name == constants.commands[5]):
            await commands.purgeChannel(msg.channel)
        else:
            await commands.sayThereIsNoSuchCommand(msg.channel)


@botClient.event
async def on_message(msg):
    if(not(utils.ifMsgOnTheChannel(msg, constants.BOT_TXT_CHANNEL_ID)) or utils.ifMsgComesFromBot(msg)):
        return
    else:
        await handleCommands(msg)

botClient.run(constants.BOT_TOKEN)
