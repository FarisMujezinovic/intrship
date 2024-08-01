import random

def initialize_board():
    return [[0 for i in range(1, 10)] for j in range(1, 10)]

# Step 2: Generation
def is_valid_number(board, row, col, number):
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False
    # 3x3 subgrid
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == number:
                return False
    return True

def generate_board(board):
    numbers = [i for i in range(1, 10)]
    random.shuffle(numbers)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for number in numbers:
                    if is_valid_number(board, i, j, number):
                        board[i][j] = number
                        if generate_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Step 3: Remove cells
def remove_cells(board):
    print("Select difficulty: easy, medium, or hard:")
    difficulty = input().lower()

    if difficulty == "easy":
        num_cells = 30
    elif difficulty == "medium":
        num_cells = 40
    elif difficulty == "hard":
        num_cells = 50
    else:
        print("You entered an invalid difficulty. Please choose easy, medium, or hard.")
        return

    while num_cells > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_cells -= 1

# Step 4: Check move
def is_valid_move(board, row, col, number):
    if board[row][col] != 0:
        return False
    return is_valid_number(board, row, col, number)

# Step 5: Print board
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

# Step 6: Play
def is_solved(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True

def play(board):
    while not is_solved(board):
        print_board(board)
        print("Enter row, column, and number (spaces between are required): ")
        row, col, number = map(int, input().split())
        if is_valid_move(board, row, col, number):
            print("Well done!")
            board[row][col] = number
        else:
            print("Invalid move. Please try again.")

# Step 7: Check solution
def is_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 or not is_valid_number(board, i, j, board[i][j]):
                return False
    return True

# Step 8: Main Function
def main():
    board = initialize_board()
    generate_board(board)
    remove_cells(board)

    print("Sudoku game:")
    play(board)

    if is_solved(board):
        print("Congratulations! Sudoku is solved.")
    else:
        print("Game over. The board is not solved.")

main()
