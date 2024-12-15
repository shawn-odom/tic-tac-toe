from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('move')
def handle_move(data):
    global board
    row, col = data['row'], data['col']
    if board[row][col] == ' ':
        board[row][col] = 'X'  # Update with player's move (change as needed)
        emit('updateBoard', board, broadcast=True)

@socketio.on('reset')
def reset_game():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    emit('updateBoard', board, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)