#  -*- coding: utf-8 -*-

import os
import pafy
import vlc
import re
import time
import youtube_dlc

def getURL(url):
    with youtube_dlc.YoutubeDL() as ydl:
        videoInfo = ydl.extract_info(url, download=False)
    return videoInfo["formats"][0]["url"]

while True:
    url = input("What is the URL? ")
    print()
    try:
        print("Getting Video URL")
        streamURL = getURL(url)
        print(streamURL)
#        video = pafy.new(url)
#        best = video.getbestaudio()
        vlcInstance = vlc.Instance()
#        playurl = best.url
        player = vlcInstance.media_player_new()
        vlcMedia = vlcInstance.media_new(streamURL)
        player.set_media(vlcMedia)
#       player = vlc.MediaPlayer(playurl)
        print(player.get_state())
        print("Playing in VLC")
        player.play()
        time.sleep(1.5)
        staticState = player.get_state()
        currentState = player.get_state()
        while currentState == staticState:
            currentState = player.get_state()
            time.sleep(3)
        print()
        print()
    except:
        print()
        print("There was an error processing that video, please try again")
        print()
        print()
