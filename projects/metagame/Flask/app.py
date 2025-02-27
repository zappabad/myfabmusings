from flask import Flask
from tournament import tournament_bp
from chane import chane_bp
import pandas as pd
from datetime import datetime
import os

def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = 'uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.register_blueprint(tournament_bp, url_prefix='/tournament')
    app.register_blueprint(chane_bp, url_prefix='/chane')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)