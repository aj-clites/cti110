# Andrew Clites
# P4LAB1A
# 2024-04-01
# A program that writes a square and triangle in a turtle graphic.

import turtle

x = 0
y = 0
while x < 4:
    turtle.forward(50)
    turtle.left(90)
    x = x + 1
    if x == 4:
        while y < 4:
            turtle.forward(50)
            turtle.left(120)
            y = y + 1

halt = input()