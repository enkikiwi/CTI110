# CTI-110
# P4LAB1a - Shapes
# Enki Sell
# November 5 2022
#
# Use turtle graphics and either a while or for loop to write a program that draws both a square and a triangle
#

import turtle

wn = turtle.Screen()

turtle.shape("turtle")

for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.penup()
turtle.forward(100)
turtle.pendown()

for i in range(3):
    turtle.forward(100)
    turtle.left(120)


