# CTI-110
# P4LAB1b - Initials
# Enki Sell
# November 5 2022
#
# Use turtle graphics to write a program that draws E S, no loop needed
#

import turtle

wn = turtle.Screen()

turtle.shape("turtle")

turtle.backward(50) # back that boy up to get the top of E
turtle.right(90) # turn boy so he can write the top half of the left of E
turtle.forward(50) # make boy write top half of the left of E
turtle.left(90) # turn boy so he can write the middle of E
turtle.forward(50) # make boy write middle of E
turtle.backward(50) # back that boy up to the spine again
turtle.right(90) # turn boy
turtle.forward(50) # go my little turty boy
turtle.left(90) # one last turn on that E
turtle.forward(50) # E complete

# time for s, gunna keep it simple

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
