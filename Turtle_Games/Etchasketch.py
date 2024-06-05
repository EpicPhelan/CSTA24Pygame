"""
Etch-a-sketch game
Arrow Keys to move
Press W to make the line wider
Press S to make the line thinner
Press D to make it faster
Press S to make it slower
Press space to clear the board
"""


import turtle
width = 1
speed = 1
draw = turtle.Turtle()
square = turtle.Turtle()
bg = turtle.Screen()
square.speed(0)
def draw_square():
    square.pu()
    square.goto(-225,125)
    square.pensize(50)
    square.color('red')
    square.pd()
    square.goto(225,125)
    square.goto(225,-175)
    square.goto(-225,-175)
    square.goto(-225,125)
    square.hideturtle()
draw_square()
square.pu()
square.pensize(100)
square.goto(-125,-175)
square.color('grey')
square.pd()
square.fd(1)
square.pu()
square.goto(125,-175)
square.pd()
square.fd(1)
square.pu()
draw.shape('circle')
square.goto(0,175)

def up():
    global speed
    y=draw.ycor()
    x=draw.xcor()
    if draw.ycor()<90:
        draw.goto(x,(y+speed))
def down():
    global speed
    y=draw.ycor()
    x=draw.xcor()
    if draw.ycor()>-140:
        draw.goto(x,(y-speed))
def left():
    global speed
    y=draw.ycor()
    x=draw.xcor()
    if draw.xcor()>-190:
        draw.goto(x-speed,y)
def right():
    global speed
    y=draw.ycor()
    x=draw.xcor()
    if draw.xcor()<190:
        draw.goto(x+speed,y)
def shake():
    draw.clear()
def wider():
    global width
    width += 1
    draw.pensize(width)
def thinner():
    global width
    if width !=1:
        width -= 1
    draw.pensize(width)
def fast():
    global speed
    if speed != 7:
        speed += 1
def slow():
    global speed
    if speed != 1:
        speed -= 1
bg.listen()
bg.onkeypress(up,"Up")
bg.onkeypress(down,"Down")
bg.onkeypress(left,"Left")
bg.onkeypress(right,"Right")
bg.onkeypress(shake,"space")
bg.onkeypress(wider,"w")
bg.onkeypress(thinner,'s')
bg.onkeypress(fast,"d")
bg.onkeypress(slow,"a")

bg.mainloop()