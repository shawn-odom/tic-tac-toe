import socket


def initialize_board():
    """Initialize the empty 3x3 game board"""
    return [[' ' for _ in range(3)] for _ in range(3)]

def format_board(board):
    """Return a formatted string of the game board"""
    return "\n".join(["|".join(row) for row in board])

def display_board(board):
    """Display current game board"""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
    """Check winner"""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 12345))

    server_socket.listen(1)
    print("Waiting for player to connect...")

    client_socket, client_address = server_socket.accept()
    print(f"Player connected: {client_address}")

    board = initialize_board()
    turn = "X"
    game_over = False

    while not game_over:
        display_board(board)
        client_socket.send(format_board(board).encode())
        try:
            move = client_socket.recv(1024).decode()
            if not move:
                print("Client disconnected.")
                game_over = True
                break
        
            row, col = map(int, move.split(','))
            if board[row][col] == ' ':
                board[row][col] = turn
            else:
                client_socket.send("Invalid move. Spot is already taken. Try again".encode())
                continue
        
            if check_winner(board):
                display_board(board)
                client_socket.send(f"Player {turn} wins!".encode())
                game_over = True
                break
        
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                display_board(board)
                client_socket.send("It's a tie".encode())
                game_over = True
                break
        
            turn = 'O' if turn == 'X' else 'X'
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()