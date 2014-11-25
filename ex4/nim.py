# Load external library
from computer_functions import get_computer_move, HEAPS

# Functions and Helpers

def empty_board(board):
    empty = True 
    for row in board:
        if row != 0:
            empty = False

    return empty 
        

def print_board(board):
    i = 1
    for row in board:
        row_var = ""
        print(str(i) + ":")
        for cell in range(0,row):
            row_var += "* "
        print(row_var.strip()) # Print board trim spaces
        i+=1

def update_board(board, row, count):
    # Receive board, row and number of matches
    # Update the board and return it
    board[row-1] -= count

    return board

def get_row(board):
    while True:
        row = int(input("Row?"))
        if row not in range(1,len(board)+1):
            # Out of bounds (row does not exist)
            next

        else:
            # Row exist
            if board[row-1] == 0:
                print("That row is empty")
                next
            else:
                break
    return(row)


def get_matches(board, row):
    while True:
        matches = int(input("How many?"))
        
        if board[row-1] < matches:
            # Too much matches!
            next
        else:
            # Return validated matches
            return(matches) 




# Game flow:
board = list(HEAPS)
n     = 1


# Choose participants
players = int(input("Please enter number of human participants (1 or 2):"))

if players == 1:
    MULTIPLAYER = False
    player1 = str(input("Please enter your name:"))
elif players == 2:
    MULTIPLAYER = True
    player1 = str(input("Name of first player:"))
    player2 = str(input("Name of second player:"))

print_board(board)


# Game starts
while True: 
    if MULTIPLAYER or n%2==1:
        if n % 2 == 1:
            current_player = player1
        else:
            current_player = player2
    
        print(current_player + ", it's your turn:")

        row = get_row(board) 
        matches = get_matches(board, row) 


    elif not MULTIPLAYER and n%2 == 0:
        current_player = "Computer"
        row, matches = get_computer_move(board)
        row+=1
        print("Computer takes " + str(matches) + " from row " + str(row))
        
    update_board(board, row, matches)
    print_board(board)

    if empty_board(board):
        print(current_player + " wins")
        play_again = input("Play again? (Y/N)")
        if play_again == "Y" or play_again == "y":
            board = list(HEAPS)
            next
        else:
            break
    else:
       n += 1 # increment






























