from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template('index.html', heading_text_one="Hello", heading_text_two="World")