#############################################################
# FILE : ex2a.py
# WRITER : Yochay Ettun , yochze,  201517018
# EXERCISE : intro2cs ex2 2014-2015
# DESCRIPTION:
# A program that gets one of three shapes (rectangle, circle or triangle) 
# then, according to the shape, the program requests more input data from
# user (edges, radius),
# and calculates shape's perimeter and area.
# The program make use  of math library. For pi, square root 
# #############################################################

import math

shape = float(input("Choose a shape:"))

if shape == 1:
    # Rectangle
    # Retrieve height and width from end-user
    # Area calculated by height*width
    # Perimeter calculated by adding all height and width and 
    # multiplying it by 2.

    # print("You have chosen rectangle!")
    width  = float(input("width:"))
    height = float(input("height:"))

    perimeter = (height+width)*2 
    area = height*width

elif shape == 2:
    # Circle
    # Retrieve radius from end-user
    # Area calculated by \pi*radius**2
    # Perimeter calculated by 2*pi*radius

    # print("You have chosen rectangle!")
    radius = float(input("radius:"))

    perimeter = (2*math.pi)*radius
    area = math.pi*(radius**2)

elif shape == 3:
    # Triangle
    # Retrieve all triangle's edges from end-user
    # Area is calcualted by Heron's Formula
    # Perimeter is a simple addition of all triangle's edges.

    # print("You have chosen: triangle!")
    ab = float(input("a:"))
    bc = float(input("b:"))
    ca = float(input("c:"))

    perimeter = ab + bc + ca

    # Calculating Area according to Heron's Formula
    s = (ab + bc + ca) / 2
    inner_equation = s*(s-ab)*(s-bc)*(s-ca) # Has to be positive
    area = math.sqrt(inner_equation)

else:
    # If initial shape input from user is unrecognized and quit program.
    print("Please enter a valid number for shape: 1 for rectangle, "
           + "2 for circle, or 3 for triangle")
    quit()


# Print results
print("area: " + str(area))
print("perimeter: " + str(perimeter))
