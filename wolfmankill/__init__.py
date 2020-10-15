from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import os

socketio = SocketIO()

def create_app(debug=True):
    # create and configure the app
    app = Flask(__name__)
    app.debug = debug
    # usage: 
    ##from flask import current_app 
    # current_app.config["SECRET_KEY"]
    app.config.from_mapping( 
        SECRET_KEY='dev'
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # app.config.from_pyfile('config.cfg', silent=True)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app