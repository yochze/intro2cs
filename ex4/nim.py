#############################################################                   
# FILE : nim.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex4 2014-2015                                             
# DESCRIPTION:                                                                  
#
# #############################################################  

# Load external library

from computer_functions import get_computer_move, HEAPS


# Functions and Helpers

def empty_board(board):
    """ Evaluates the board and returns if empty or not
        input is an list representing the board
        output is boolean """
    empty = True 
    for row in board:
        if row != 0:
            empty = False

    return empty 
        

def print_board(board):
    """ Printing the board in the following format:
        1. 
        * * *
        2. 
        * * * *, etc..
        
        Flow: Goes through each cell in the list and prints the index with 
        a newline then creating a new string that has n times "* ", 
        where n is the value in the list[index].
        
        Input: Array representing the board
        Output: Formatted board. """
    i = 1
    for row in board:
        row_var = "" # Reset string of each row
        print(str(i) + ":")
        for cell in range(0,row):
            row_var += "* " # Add "* " 
        print(row_var.strip()) # Print row with trim spaces (strip func)
        i+=1

def update_board(board, row, matches):
    """ Upadting the board according the user's play.
        Input: board, row, matches
        Output: The updated board with the recent play. """
    board[row-1] -= matches 

    return board

def get_row(board):
    """ This function handles the request of user row input.
        It does the actual request and validates the user input.
        Until a validated row number will enter, it keeps asking the user
        for a new row number.

        Input:  List representing the board
        Output: Returns row number after fully validated """
    while True:
        row = int(input("Row?"))
        if row not in range(1,len(board)+1):
            # Out of bounds (row does not exist)
            next

        else:
            # Row exist
            if board[row-1] == 0:
                # Empty row, print error, and continue asking for row number.
                print("That row is empty")
                next
            else:
                break
    return(row)


def get_matches(board, row):
    """ This function handles the request of user matches input.
        It does the actual request and validates the user input.
        Until a validated matches count will enter, it keeps asking the user
        for a new sum of matches.

        Input:  Board and row number
        Output: Returns matches count after fully validated """
    while True:
        matches = int(input("How many?"))
        
        if board[row-1] < matches:
            # Too much matches!
            next
        else:
            # Return validated matches
            return(matches) 

def play_again():
    """ Asks the user for another match. 
        If the user enters Y(or y) it sets a True boolean for return 
        
        Input: Any string (Y/y for another match)
        Output: Boolean """

    play_again = str(input("Play again? (Y/N)"))
    if play_again == "Y" or play_again == "y":
        return True
    else: 
        return False


def print_win_message(player, multiplayer):
    """ Print the necassery winning message.
        Input: The winning player, and the status of the game (multiplayer)
        Output: Returning nothing, but printing the wanted message from func.
    """

    if not multiplayer and (player != "Computer"):
        print("You win")
    else: 
        print(player + " wins")


# Game flow and process

def play_game(player1, player2=None):
    
    MULTIPLAYER = False if player2 == None else True 
    board = list(HEAPS)
    n     = 1
    
    print_board(board)

    while True: 
        if MULTIPLAYER or (n%2 == 1):
            if n % 2 == 1:
                current_player = player1
            else:
                current_player = player2
        
            print(current_player + ", it's your turn:")

            row = get_row(board) 
            matches = get_matches(board, row) 


        elif not MULTIPLAYER and (n%2 == 0):
                # Computer always second at first
                current_player = "Computer"
                row, matches = get_computer_move(board)
                row += 1
                print("Computer takes " + str(matches) + " from row " + str(row))
            
        update_board(board, row, matches)
        print_board(board)

        if empty_board(board):
            print_win_message(current_player, MULTIPLAYER)
            
            if play_again():
                board = list(HEAPS)
                print_board(board)
                next
            else: 
                break

        else:
           n += 1 # increment


# Program Flow:

# Choose number of human players
players = int(input("Please enter the number of human players (1 or 2):"))

if players == 1:
    # Run the gmae of single player and one automatic player (computer).
    player1     = str(input("Please enter your name:"))
    play_game(player1)


elif players == 2:
    # Run the game for two human players.
    player1     = str(input("Name of first player:"))
    player2     = str(input("Name of second player:"))
    
    play_game(player1, player2)

