def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
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

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")

        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()