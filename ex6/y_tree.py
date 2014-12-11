#############################################################
# FILE : y_tree.py
# WRITER : Yochay Ettun , yochze
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# A recursive function that uses the turtle external library to
# draw a binary tree in the size of the user input (or default: 200).
#############################################################

import turtle # Library for graphcics

def draw_tree(length=200):
    """
    A recursive function that uses the turtle external library to
    draw a binary tree in the size of the user input (or default: 200).

    The flow of the function that it first draw a straight line,
    the right side branches and then left side branches.
    """
    # length is number of pixel 
    deg = 30 # degrees of each branch (left, right)

    if not length < 10:
        # Base is when the length is lower then 10,
        # otherwise, continue with the iteration.

        turtle.forward(length)  # Draw straight line forward size length 
        turtle.right(deg)       # Turn right 30 degrees
        draw_tree(length*0.6)   # Call the recursion to draw the right
                                # side branches

        turtle.left(deg*2)      # Then turn left (30 degrees center,
                                # 30 degrees more to the left)
        draw_tree(length*0.6)   # Draw inner left side branches

        turtle.right(deg)       # Turn to center
        turtle.backward(length) # Go backwards length size


# Call the function, default is set to 200.
draw_tree()
