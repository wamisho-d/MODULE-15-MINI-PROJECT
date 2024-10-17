# 1. WebSocket Setup and Configuration:
# install the necessary libraries:
# pip install flask-socketio
# pip install eventlet # For asynchronous handling

# Basic server configuration
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)

# 2. Implementing WebSocket Events and Handlers
# Connection Event: 
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', {'data': 'Welcome to the chat!'})

# Message Event:
@socketio.on('send_message')
def handle_message(data):
    print('Recieved message: ' + data['message'])
    emit('recieve_message', {'message': data['message']}, broadcast=True)

# Disconnection Event:
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

