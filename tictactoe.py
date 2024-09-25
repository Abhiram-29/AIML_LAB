import math
def check_winner(board):
    winning_combinations = [
        [board[0], board[1], board[2]],  # Row 1
        [board[3], board[4], board[5]],  # Row 2
        [board[6], board[7], board[8]],  # Row 3
        [board[0], board[3], board[6]],  # Column 1
        [board[1], board[4], board[7]],  # Column 2
        [board[2], board[5], board[8]],  # Column 3
        [board[0], board[4], board[8]],  # Diagonal 1
        [board[2], board[4], board[6]]   # Diagonal 2
    ]
    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] and combination[0] != ' ':
            return combination[0]
    return None
def is_full(board):
    return ' ' not in board
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 10 - depth, None
    elif winner == 'O':
        return depth - 10, None
    elif is_full(board):
        return 0, None
    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score, _ = minimax(board, depth + 1, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score, _ = minimax(board, depth + 1, True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move
def find_best_move(board):
    score, best_move = minimax(board, 0, True)
    return best_move, score
def print_board(board):
    for i in range(3):
        print(board[3 * i], '|', board[3 * i + 1], '|', board[3 * i + 2])
        if i < 2:
            print('---------')
def play_game():
    board = [' '] * 9
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            move, score = find_best_move(board)
            print(f"AI chooses position {move + 1} with optimal cost {score}")
        else:
            move = int(input("Enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
play_game()