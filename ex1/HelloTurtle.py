#############################################################
# FILE : HelloTurtle.py
# WRITER : Yochay Ettun,  yochze, 201517018
# EXERCISE : intro2cs ex1 2014-2015
# DESCRIPTION:
# A program that draw some simple geometric shapes on the screen
# and prints  "Hello Turtle", using Turtle graphics
#############################################################

import turtle

# Start off
turtle.title('Fun with Turtle Graphics and Python') # Set title for display
turtle.up() # Lift the pen, i.e no drawing
turtle.goto(-100, -100) # Go to spot
turtle.down() # Put pen down !


# Red square
turtle.pencolor('red') # Set pen color to red
turtle.goto(-100,100)  # Top right
turtle.goto(100,100)   # Top left
turtle.goto(100,-100)  # Bottom left
turtle.goto(-100,-100) # Bottom right

# Circle
turtle.goto(0,-100)
turtle.pencolor('orange') # Set pen color to red
turtle.circle(100)

# Large square
turtle.up() # Stop drawing
turtle.goto(-200,0) # Goto first position of drawing large square
turtle.pencolor('blue') # Set pencolor to blue
turtle.down() # Start drawing
turtle.goto(0,200)
turtle.goto(200,0)
turtle.goto(0,-200)
turtle.goto(-200,0)

# Text
turtle.up() # Stop drawing
turtle.goto(-70,-5) # Set initial position for text
turtle.pencolor('green') # Change color to green
turtle.write("Hello Turtle!", font=("Arial", 20, "normal")) # Write text

# Finalize
turtle.done() 
