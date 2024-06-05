'''
Maze template for an example

'''
import turtle

#background
window = turtle.Screen()
#rgb color triplets
window.colormode(255)
window.bgcolor(255,80,140)

#window.bgcolor(0,0,0) for rgb
#Tim is the maze runner
tim = turtle.Turtle()
tim.shape("turtle")
tim.pu()
tim.goto(13,-200)
tim.left(90)


#Maze builder
maze = turtle.Turtle()
maze.hideturtle()
maze.speed(0)



#square function
def square(x,y):
    maze.pu()
    maze.goto(x,y)
    maze.pd()
    maze.pencolor("darkblue")
    maze.fillcolor("lightBlue")
    maze.begin_fill()
    for i in range(4):
        maze.forward(25)
        maze.right(90)
    maze.end_fill()


def drawmaze():
    #left wall
    yval = -150
    for i in range(15):
        if yval == 200:
            yval += 25
            continue
        else:
            square(-200,yval)
            yval += 25
    #top wall
    xval = -200
    for i in range(16):
        square(xval, 225)
        xval += 25
    #right wall
    yval = 225
    for i in range(16):
        square(200,yval)
        yval -= 25
    #bottom wall
    xval = 200
    for i in range(16):
        if xval == 0:
            xval -= 25
            continue
        else:
            square(xval,-150)
            xval -= 25
    #write end
    maze.pu()
    maze.goto(-225,180)
    maze.pd()
    maze.write("end")
    #write start
    maze.pu()
    maze.goto(-25,-200)
    maze.pd()
    maze.write("start")
    #maze filling
    yval = -125
    for i in range(5):
        square(-75,yval)
        yval += 25
    square(-50,-100)
    square(-25,-100)
    square(-25,-75)
    square(-25,-50)
    square(-25,-25)
    square(0,-25)
    #square(25,-25)
    square(50,-25)
    square(50,0)
    square(25,-100)
    xval = 50
    for i in range(5):
        if xval == 75:
            xval += 25
            continue
        else:
            square(xval,-100)
            xval += 25
    square(25,-75)
    square(50,-75)
    square(50,-50)
    #square(50,50)
    square(50,25)
    square(25,25)
    xval = 0
    for i in range(6):
        if xval == -100:
            xval -= 25
            continue
        else:
            square(xval,25)
            xval -= 25
    yval = -175
    square(125,-75)
    square(125,-50)
    square(125,-25)
    square(125,0)
    square(75,-50)
    square(100,0)
    square(100,25)
    square(100,50)
    square(125,50)
    square(125,75)
    square(175,25)
    square(175,-25)
    square(175,-50)
    square(175,75)
    square(175,100)
    square(175,125)
    square(150,125)
    #square(150,150)
    square(100,75)
    square(100,100)
    square(100,125)
    #square(100,150)
    square(100,175)
    square(125,175)
    square(150,175)
    square(150,200)
    square(75,125)
    square(75,175)
    square(25,175)
    square(25,150)
    square(25,125)
    #square(25,100)
    square(25,75)
    #square(50,75)
    square(75,75)
    square(50,75)
    square(0,75)
    square(0,100)
    square(0,125)
    square(-25,200)
    square(-25,175)
    square(-50,175)
    square(-75,175)
    square(-50,150)
    square(-50,125)
    square(-25,75)
    square(-50,75)
    square(-100,100)
    #square(-100,125)
    square(-100,150)
    square(-100,175)
    square(-100,75)
    #square(-75,75)
    #square(-125,100)
    #square(-150,100)
    square(-150,125)
    square(-150,150)
    square(-150,175)
    square(-150,200)
    square(-125,75)
    square(-150,75)
    square(-150,50)
    square(-150,25)
    square(-150,0)
    square(-150,-25)
    square(-125,-25)
    square(-25,0)
    square(-50,50)
    square(-125,-50)
    square(-125,-75)
    square(-150,-75)
    square(-150,-100)
    square(-125,-100)
    square(-125,-125)

drawmaze()

# Students can program Tim to run the maze or use the arrow keys to move him

window.mainloop()