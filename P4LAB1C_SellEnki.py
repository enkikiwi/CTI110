# CTI-110
# P4LAB1c - Snowflake
# Enki Sell
# November 5 2022
#
# Use turtle graphics and a range function to write a program that draws a snowflake
#
# I PROBABLY MADE THIS WAY TOO COMPLICATED BUT I WANTED TO TRY ANYWAY

import turtle

wn = turtle.Screen()

turtle.shape("turtle")

for i in range(4):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(45)
    turtle.forward(75)
    turtle.backward(75)
    turtle.left(45)
for i in range(4):
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(15)
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(15)
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(45)
    turtle.backward(100)
    turtle.left(90)

for i in range(4):
    turtle.left(45)
    turtle.forward(37.5)
    turtle.left(45)
    turtle.forward(15)
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(45)
    turtle.forward(37.5)
    turtle.left(45)
    turtle.forward(15)
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(45)
    turtle.backward(75)
    turtle.left(45)
