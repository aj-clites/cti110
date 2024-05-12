# Andrew Clites
# P4LAB1B
# 2024-04-01
# A program that writes the initials AC in a turtle graphic.
import turtle

turtle.color("blue")
turtle.pensize(3)

x = 1

for x in range(0,1):
    turtle.left(65)
    turtle.forward(50)
    turtle.right(127)
    turtle.forward(50)
    turtle.penup()
    turtle.left(155)
    turtle.forward(26)
    turtle.left(90)
    turtle.forward(12)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.pendown()
    turtle.color("purple")
    turtle.left(180)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    x = x + 1

halt = input()