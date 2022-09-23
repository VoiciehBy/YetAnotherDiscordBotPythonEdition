import constants
import discord
import youtube_dl
from youtube_search import YoutubeSearch


def getSongs(searchTerm):
    return YoutubeSearch(searchTerm, max_results=1).to_dict()

def music_url(song_name):
    songs = getSongs(song_name)
    
    if(songs):
        ytUrl = "https://www.youtube.com/"
        song = songs[0]
        url = str(ytUrl+song.get("url_suffix"))
        return url
    else:
        return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def song_title(url):
    songs = getSongs(url)

    if(songs):
        song = songs[0]
        title = str(song.get("title"))
        return title
    else:
        return "None"

def download_music(url):
    d_m_d_e = constants.default_music_download_extension
    ytdl_opts = {"format": "bestaudio[ext=" + d_m_d_e + ']',
                 "embeded-thumbnail": True,
                 "add-metadata": True,
                 "outtmpl": constants.musicDirPath + f"%(title)s" + ".%(ext)s"}
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download([url])
    return constants.musicDirPath+song_title(url)+'.' + d_m_d_e


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
        cH += constants.PREFIX + \
            constants.commands[i] + " - " + constants.commands_desc[i] + "\n"
    return cH


def getVoiceChannel(botClient):
    return botClient.get_channel(constants.BOT_VOICE_CHANNEL_ID)


def ifMsgOnTheChannel(msg, channelId):
    return msg.channel.id == channelId