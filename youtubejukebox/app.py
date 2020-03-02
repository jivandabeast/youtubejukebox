from flask import Flask
from youtubejukebox.views.index import bp as index_bp
from youtubejukebox.views.createnote import bp as createnote_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createnote_bp)


