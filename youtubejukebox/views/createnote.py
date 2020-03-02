from flask import Blueprint, render_template, request, redirect
from subprocess import call
import os
import pafy

bp = Blueprint(__name__, __name__, template_folder='templates')


def random_string(length=16):
    i = 1
    current_wd = os.getcwd()
    os.chdir("youtubejukebox/notes")
    while os.path.exists("song%s.note" % i):
        i += 1
    final_string = i
    os.chdir(current_wd)
    return final_string

def download_song(arg1):
    print(arg1)
    url = pafy.new(arg1)
    title = url.title
    bestaudio = url.getbestaudio()
    current_wd = os.getcwd()
    os.chdir("youtubejukebox/songs")
    bestaudio.download()
    os.chdir(current_wd)
    play_song(title)
    return title

def play_song(arg1):
    current_wd = os.getcwd()
    os.chdir("youtubejukebox/songs")
    call(["./addtovlc.sh", arg1])
    os.chdir(current_wd)

@bp.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
            song_request = request.form.get('notetext')
#            text = request.form.get('notetext')
            with open('youtubejukebox/notes/song{}.note'.format(random_string()), 'w+') as _file:
                _file.write(download_song(song_request))
            _file.close()
            return redirect('/')
    return render_template('createnote.html')