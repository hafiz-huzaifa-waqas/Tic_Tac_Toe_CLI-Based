import random

# --- draw the board ---
def display(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


# check if someone won
def check_win(board, sign):
    win_patterns = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for pattern in win_patterns:
        if all(board[r][c] == sign for r, c in pattern):
            return True
    return False


# check if the board is full 
def board_full(board):
    for row in board:
        for val in row:
            if val not in ['X', 'O']:
                return False
    return True


# --- user move ---
def user_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                raise ValueError
        except ValueError:
            print("Invalid move. Try again.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("That spot is already taken!")
        else:
            board[row][col] = 'O'
            break


# --- computer move ---
def computer_move(board):
    free_spaces = []

    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_spaces.append((r, c))

    if free_spaces:
        r, c = random.choice(free_spaces)
        board[r][c] = 'X'


# ----------------------------------------------------
# ------------------- GAME START ---------------------
# ----------------------------------------------------

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],  
    ['7', '8', '9']
]

display(board)

while True:

    user_move(board)
    computer_move(board)
    display(board)

    if check_win(board, 'O'):
        print("You won!")
        break

    if board_full(board):
        print("It's a tie!")
        break

    if check_win(board, 'X'):
        print("Computer won!")
        break
    
   
