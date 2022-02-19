import constants
import discord


def ifMsgComesFromBot(msg):
    return msg.author.bot


def isCommmand(msg):
    return msg.content[0] == (constants.PREFIX) and msg.channel.id == constants.BOT_TXT_CHANNEL_ID


def getCommandName(msg):
    if (msg.content.find(' ') != -1):
        return msg.content[(len(constants.PREFIX)):msg.content.find(' ')]
    elif(len(msg.content) > 1):
        return msg.content[(len(constants.PREFIX)):]
    else:
        return constants.PREFIX

def getCommandArguments(msg):
    if (len(msg.content) > 1):
        return msg.content.strip()[msg.content.find(' ')+1:]
    else:
        return " "


def commandsHelp():
    cH = ""
    i = 0
    for i in range(0, (len(constants.commands))):
        cH += constants.PREFIX + constants.commands[i] + " - " + constants.commands_desc[i] + "\n"
    return cH


def getVoiceChannel(botClient):
    return botClient.get_channel(constants.BOT_VOICE_CHANNEL_ID)


def ifMsgOnTheChannel(msg, channelId):
    return msg.channel.id == channelId
