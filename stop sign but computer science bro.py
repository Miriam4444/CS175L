import math
import turtle

#variable names
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

#size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

#turtle.pensize(10)

#center turtle
turtle.penup()
turtle.goto(-50, (diameter/2))
turtle.pendown()

#make it red
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()

for i in range(8):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()

 #white octagon
def white_octagon():
    NUM_SIDES = 8
    LENGTH = 90
    ANGLE = 45
    TEXT_X = -5
    TEXT_Y = -10
    s = LENGTH
    x = s / math.sqrt(2)
    diameter = s + (2 * x)
    turtle.color("white")
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-45, (diameter/2))
    turtle.pendown()
    for i in range(8):
        turtle.forward(LENGTH)
        turtle.right(ANGLE)

white_octagon()

turtle.penup()
turtle.goto(0,-36)
turtle.pendown()
turtle.write("STOP" , align = 'center' , font = ("Arial" , 48 , "bold"))




