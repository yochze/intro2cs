##
# python

import turtle

def draw_tree(length=200):
    # length is number of pixel 
    deg = 30

    if not length < 10:
        turtle.forward(length)
        turtle.right(deg)
        draw_tree(length*0.6)

        turtle.left(deg*2)
        draw_tree(length*0.6)

        turtle.right(deg)
        turtle.backward(length)

draw_tree()
