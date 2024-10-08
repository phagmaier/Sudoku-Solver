def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and pos[1] != j:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Example usage
board = [
    [0, 0, 0, 3, 7, 0, 0, 2, 0],
    [0, 9, 0, 0, 8, 5, 7, 0, 0],
    [3, 0, 0, 9, 0, 0, 0, 0, 5],
    [1, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [2, 0, 0, 6, 0, 0, 0, 0, 1],
    [0, 4, 8, 0, 0, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 4, 0]
]

print("Original Sudoku board:")
print_board(board)
print("\nSolving...\n")

if solve_sudoku(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists")
