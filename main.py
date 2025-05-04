import math

# Board Representation
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for winner
def check_winner(brd, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diags
    ]
    return any(all(brd[pos] == player for pos in combo) for combo in win_combinations)

def is_draw(brd):
    return ' ' not in brd

# Minimax algorithm
def minimax(brd, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move1
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'

        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI has made a move:")
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()