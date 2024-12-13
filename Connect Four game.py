

def print_board(board):
    for row in board:
        row_str = " | ".join(row)
        print(row_str)
        print("-" * (len(row_str) + 2))

def get_move(turn, board):
    while True:
        col = int(input(f"Player {turn}, select a column (1-{len(board[0])}): ")) - 1
        
        if col < 0 or col >= len(board[0]):
            print("Invalid column, try again.")
            continue
            
        # Check for the lowest empty spot in the selected column
        for row in reversed(board):
            if row[col] == " ":
                row[col] = turn
                return
        print("Column is full, try again.")

def check_win(board, turn):
    # Check horizontal, vertical, and diagonal connections
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (col + 3 < len(board[0]) and 
                    all(board[row][col + i] == turn for i in range(4))):
                return True
            if (row + 3 < len(board) and 
                    all(board[row + i][col] == turn for i in range(4))):
                return True
            if (row + 3 < len(board) and col + 3 < len(board[0]) and
                    all(board[row + i][col + i] == turn for i in range(4))):
                return True
            if (row - 3 >= 0 and col + 3 < len(board[0]) and
                    all(board[row - i][col + i] == turn for i in range(4))):
                return True
    return False

# Initialize the board
board = [[" " for _ in range(7)] for _ in range(6)]
turn = "X"
turn_number = 0
max_turns = len(board) * len(board[0])
print_board(board)

# Main game loop
while turn_number < max_turns:
    print()
    get_move(turn, board)
    print_board(board)
    
    if check_win(board, turn):
        print(f"Player {turn} wins!")
        break
    
    # Switch turns
    turn = "O" if turn == "X" else "X"
    turn_number += 1

if turn_number == max_turns:
    print("It's a tied game!")

