import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0

def make_a_shape():
    import math
    import turtle
    #variable names
    a = int(input("How many sides do you want? "))
    b = int(input("Choose a side length "))
    NUM_SIDES = a
    LENGTH = b
    ANGLE = 360 / NUM_SIDES
    #size the window
    turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    s = LENGTH
    #x = s / math.sqrt(2)
    #diameter = s + (2 * x)

    half_angle = ANGLE / 2
    y_coordinate = math.tan(half_angle * (180 /math.pi)) * (s / 2)
    #format shape
    outline_color = input("Choose an outline color ")
    fill_color = input("Choose a fill color ")
    pen_size = int(input("Choose a pen size "))
    turtle.color(outline_color)
    turtle.fillcolor(fill_color)
    turtle.pensize(pen_size)
    turtle.begin_fill()
    #center turtle
    turtle.penup()
    turtle.goto((-s / 2), y_coordinate)
    turtle.pendown()
    #make shape
    for i in range(NUM_SIDES):
        turtle.forward(LENGTH)
        turtle.right(ANGLE)
    turtle.end_fill()
    #go back to (0,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    
    

for i in range(2):
    print(f"octagon #{i+1}: ")
    make_a_shape()

#write text
words = input("Do you want text? ")
if words == "yes":
    size = int(input("Choose font size: "))
    text = input("Enter text: ")
    y = int((size / 4) * 3)
    turtle.penup()
    turtle.goto(0,-y)
    turtle.pendown()
    turtle.write(text , align = 'center' , font = ("Arial" , size , "bold"))
else:
    print("Okay.")
 

