from flask_socketio import emit
from .. import socketio
import threading
from time import sleep

values = {
    'slider1': 25,
    'slider2': 0,
}


threadLock = threading.Lock()

@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})


global vote_counter
vote_counter = 0
global votes
votes = {'player1':0, 'player2':0, 'player3':0, 'player4':0}

@socketio.on('Slider value changed')
def value_changed(message):
    global votes
    global vote_counter
    votes[message['data']] += 1
    print(message)
    with threadLock:
        vote_counter += 1
        if vote_counter == 4:
            vote_counter = 0
            emit('update value', votes, broadcast=True)
            votes = {'player1':0, 'player2':0, 'player3':0, 'player4':0}

@socketio.on('done speaking')
def done_speaking():
    sleep(5)
    emit('speak')