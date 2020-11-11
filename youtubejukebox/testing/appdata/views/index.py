from flask import Blueprint, render_template, request, redirect

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/', methods=['POST','GET'])
def show():
    if request.method == 'POST':
        if request.form.get('linkSubmit'):
            songRequest = request.form.get('songLink')
            print('Processing Request')
            print(songRequest)
            return redirect('/')
    return render_template('index.html', heading_text_one="Hello", heading_text_two="World")