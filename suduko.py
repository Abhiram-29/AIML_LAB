def print_board(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True
def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
def get_board_input():
    print("Enter the Sudoku puzzle, one row at a time. Use 0 for empty cells.")
    board = []
    for i in range(9):
        while True:
            try:
                row_input = input(f"Enter row {i + 1} (space-separated numbers): ")
                row = list(map(int, row_input.split()))
                if len(row) != 9:
                    raise ValueError("Each row must have exactly 9 numbers.")
                board.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return board
board = get_board_input()

print("\nInitial Sudoku Board:")
print_board(board)
if solve_sudoku(board):
    print("\nSolved Sudoku Board:")
    print_board(board)
else:
    print("No solution exists.")