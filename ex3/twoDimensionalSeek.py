#############################################################                   
# FILE : twoDimensionalSeek.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Logging the turns and steps of Sam and Frodo on their way to their
# destiny. Eventually the program will evaluate Gandalf way to the
# same destiny as he can fly directly, almost without turns.
# #############################################################  

# Set default values
right, forward      = 0, 0
right_or_left       = "right"
forward_or_backward = "forward"

# First position orientation is default to forward
position = "FORWARD"

# Orientation:
#
#      FORWARD 
# LEFT    +     RIGHT
#      BACKWARD

while True:
    # Iteration runs until user input is "end". 
    # until then, it first asks for direction of the next turn
    # and then the number of steps.
    # Each direction of turn changes the orientation position of Sam and Frodo
    # therefor the position variable changes accordingly based on the 
    # orientation illustration above.
    
    # Input from user
    direction = str(input("Next turn:"))

    if direction == "right":
        # For turning right, asking the number of steps
        # and setting the new position based on the previous
        # and the illustration.
        # incrementing or decrementing right/forward var steps count
        # based on the orientation (if it's real right or perhaps left).
        steps = int(input("How many steps?"))

        if position == "FORWARD":
            position = "RIGHT"
            right += steps

        elif position == "RIGHT":
            position = "BACKWARD"
            forward -= steps # Go backwards (minus forward is backwards)

        elif position == "BACKWARD":
            position = "LEFT"
            right -= steps # Go left (minus right is left)

        elif position == "LEFT":
            position = "FORWARD"
            forward += steps
        
    elif direction == "left":
        # Same logic for the left turn, according to the previous stored 
        # position it sets the new position and increment/decrement 
        # right/forward based on the orientation.
        steps = int(input("How many steps?"))

        if position == "FORWARD":
            position = "LEFT"
            right -= steps  # Go left (minus right is left)

        elif position == "RIGHT":
            position = "FORWARD"
            forward += steps

        elif position == "BACKWARD":
            position = "RIGHT"
            right += steps

        elif position == "LEFT":
            position = "BACKWARD"
            forward -= steps # Go backwards (minus forward is backwards)


    elif direction == "end":
        # Ending quest, starting calculation for Gandalf path
        # and preparing printing results.

        if right < 0:
            # Determining whether printing "left" or "right" 
            # according to which of them is larger.
            right_or_left = "left"

        if forward < 0:
            # Determining whether printing "forward" or "backward" 
            # according to which of them is larger.
            forward_or_backward = "backward"

        print('Gandalf should fly ' + str(abs(right)) + ' steps ' 
                + right_or_left + ' and ' + str(abs(forward))
                + ' steps ' + forward_or_backward)
        break
