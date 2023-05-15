## Tic Tac Toe

# Initialize the board
board = [' ' for i in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Function to check for a win
def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

# Function to check if the board is full
# def check_full():
    if ' ' not in board:
        return True
    return False

# Main game loop
print('Welcome to Tic Tac Toe!')
print_board()

while True:
    # Player 1's turn
    choice = int(input("Player 1's turn (choose a position from 1-9): ")) - 1
    while board[choice] != ' ':
        choice = int(input('That position is already taken. Please choose another: ')) - 1
    board[choice] = 'X'
    print_board()
    if check_win():
        print('Congratulations! Player 1 wins!')
        break
    if check_full():
        print('The game is a tie!')
        break

    # Player 2's turn
    choice = int(input("Player 2's turn (choose a position from 1-9): ")) - 1
    while board[choice] != ' ':
        choice = int(input('That position is already taken. Please choose another: ')) - 1
    board[choice] = 'O'
    print_board()
    if check_win():
        print('Congratulations! Player 2 wins!')
        break
    if check_full():
        print('The game is a tie!')
        break