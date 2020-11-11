#  -*- coding: utf-8 -*-

import vlc
import time
import youtube_dlc
from threading import Thread
from queue import Queue

def getURL(url):
    ydl_opts = {
        'quiet':True
    }
    with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
        videoInfo = ydl.extract_info(url, download=False)
    return videoInfo["formats"][0]["url"]

def playSong(q):
    vlcInstance = vlc.Instance()
    player = vlcInstance.media_player_new()
    while True:
        inputURL = q.get()
        streamURL = getURL(inputURL)
        vlcMedia = vlcInstance.media_new(streamURL)
        player.set_media(vlcMedia)
        player.play()
        time.sleep(1.5)
        staticState = player.get_state()
        currentState = player.get_state()
        while currentState == staticState:
            currentState = player.get_state()
            time.sleep(1)
        q.task_done


q = Queue(maxsize=0)
worker = Thread(target=playSong, args=(q,))
worker.setDaemon(True)
worker.start()

while True:
    url = input("What is the URL? ")
    try:
        getURL(url)
        q.put(url)
    except:
        print("Failed to parse " + str(url))
    print()
