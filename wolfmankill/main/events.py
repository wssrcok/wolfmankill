from flask_socketio import emit
from .. import socketio

values = {
    'slider1': 25,
    'slider2': 0,
}

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('Slider value changed')
def value_changed(message):
    # values[message['who']] = message['data']
    print(message)
    # emit('update value', message, broadcast=True)
