from flask import Blueprint, render_template
from os.path import expanduser
import glob
bp = Blueprint(__name__, __name__, template_folder='templates')
home = expanduser("~")

def fetch_notes():
    final_notes = []
    notes = sorted(glob.glob('youtubejukebox/notes/*.note'))
    for note in notes:
        with open(note) as _file:
            final_notes.append(_file.read())
        _file.close()
    return final_notes

def fetch_np():
    np_file = home + "/.local/share/vlc/np_title.txt"
    with open(np_file) as _file:
        now_playing = _file.read()
    _file.close()
    return now_playing


@bp.route('/')
def show():
    return render_template('index.html', notes=fetch_notes(), now_playing=fetch_np())
