import vlc
import time
import youtube_dlc
from flask import Flask, render_template, request, redirect
from threading import Thread
from queue import Queue

app = Flask('__name__')


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


def addSong(url):
    try:
        getURL(url)
        q.put(url)
        return True
    except:
        print("Adding song failed")
        return False


q = Queue(maxsize=0)
worker = Thread(target=playSong, args=(q,))
worker.setDaemon(True)
worker.start()


@app.route('/', methods=['POST', 'GET'])
def index():
    print("we inside the index func")
    if request.method == 'POST':
        if request.form.get('songlink'):
            songRequest = request.form.get('songlink')
            print('Processing Request ' + songRequest)
            print()
            if addSong(songRequest):
                return render_template('index.html', heading_text_one="Added", heading_text_two=songRequest)
            else:
                return render_template('index.html', heading_text_one="Couldn't", heading_text_two="Add")
        else:
            return render_template('index.html', heading_text_one="Uh", heading_text_two="Oh")
    else:
        return render_template('index.html', heading_text_one="Hello", heading_text_two="World!")

if __name__ == "__main__":
    app.run(debug=True)