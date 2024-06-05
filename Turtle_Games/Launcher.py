"""
Tanks game made with my students
Controls are up, down, left, right, space
Adjust angle and power
"""

import turtle,math,random

# Variables for Launcher data and score system
power = 5
amount = 5
point = 0
angle = 45
circles = []

# Creates the background
bg = turtle.Screen()
bg.bgcolor('sky blue')

# Creates the launcher
launcher = turtle.Turtle()
launcher.speed(0)
launcher.pu()
launcher.goto(-290,-93)
launcher.tiltangle(180)
launcher.setheading(angle)
launcherbottom = turtle.Turtle()
launcherbottom.speed(0)
launcherbottom.shape('triangle')
launcherbottom.pu()
launcherbottom.goto(-290,-99)
launcherbottom.tiltangle(90)
launcherbottom.shapesize(0.5)

# Shows how much ammo there is
ammo = turtle.Turtle()
ammo.speed(0)
ammo.hideturtle()
ammo.pu()
ammo.goto(-290,-93)
ammo.pd()

# Creates the ground
ground = turtle.Turtle()
ground.speed(0)
ground.pu()
ground.goto(-375,-100)
ground.pd()
ground.begin_fill()
ground.goto(375,-100)
ground.goto(375,-250)
ground.goto(-375,-250)
ground.end_fill()

# Creates the target and moves it to a random location on the ground
target = turtle.Turtle()
target.speed(0)
target.shape('square')
target.pu()
target.goto(random.randrange(-200,300),-95)

# Writes the power level
powerlevel = turtle.Turtle()
powerlevel.speed(0)
powerlevel.hideturtle()
powerlevel.pu()
powerlevel.goto(0,50)
powerlevel.write(f'The power level is {power}')

# Tells if the ammo is being launched
ammo.launching = False

# Writes how many points you have
points = turtle.Turtle()
points.speed(0)
points.hideturtle()
points.pu()
points.goto(-300,150)
points.write(point, font=('Arial',30,'normal','bold'))

# Writes how much ammo is left
ammleft = turtle.Turtle()
ammleft.speed(0)
ammleft.hideturtle()
ammleft.pu()
ammleft.goto(0,75)
ammleft.write(f'You have {amount} shot(s) left')

# Writes the angle that the launcher is at
degrees = turtle.Turtle()
degrees.speed(0)
degrees.pu()
degrees.hideturtle()
degrees.goto(-335,-100)
degrees.write(str(angle)+'°',font=('Arial',15,'normal','bold'))

# Turns the launcher clockwise by one degree
def turnright():
    global angle
    if ammo.launching == False:
        if angle > 0:
            angle -= 1
            launcher.setheading(angle)
            degrees.clear()
            degrees.write(str(angle)+'°',font=('Arial',15,'normal','bold'))

# Turns the launcher counterclockwise by one degree
def turnleft():
    global angle
    if ammo.launching == False:
        if angle <90:
            angle +=1
            launcher.setheading(angle)
            degrees.clear()
            degrees.write(str(angle)+'°',font=('Arial',15,'normal','bold'))
def velocityfind(power,angle):
    # Uses Physics to calculate X and Y velocity
    hyp = 0
    yvels = []
    yvel = power*math.sin(angle*math.pi/180)
    xvel = power*math.cos(angle*math.pi/180)
    while hyp >= 0:
        yvels.append(yvel)
        hyp += yvel
        yvel-=0.098
    return xvel,yvels
# Launches the ammo
def launch():
    global angle,power,circles,amount,point
    if amount != 0:
        if ammo.launching == False:
            xvelocity,yvelocities = velocityfind(power,angle)
            print(xvelocity,yvelocities[0])
            for i in yvelocities:
                ammo.goto(ammo.xcor()+xvelocity,ammo.ycor()+i)
            ammo.launching = False
            #Creates the hole in the ground
            circle = turtle.Turtle()
            circle.shapesize(0.001)
            circle.speed(0)
            circle.shape('circle')
            circle.color('sky blue')
            circle.pu()
            circle.goto(ammo.xcor(),ammo.ycor())
            circle.shapesize(3)
            circles.append(circle)
            #Resets the launcher positions to re-render them over the inpact area
            launcher.rt(1)
            launcher.lt(1)
            launcherbottom.goto(-290,-99)
            degrees.clear()
            degrees.write(str(angle)+'°',font=('Arial',15,'normal','bold'))
            #moves ammo back into the launcher
            ammo.clear()
            ammo.pu()
            ammo.goto(-290,-93)
            ammo.pd()
            amount -= 1
            ammleft.clear()
            ammleft.write(f'You have {amount} ammo left')
    if amount == 0:
        ammleft.clear()
        ammleft.write(f'You are out of ammo! press "R" to retry')
    #checks if any of the circles are touching the target
    for i in circles:
        if i.distance(target)<40:
            point+=1
            points.clear()
            points.write(point, font=('Arial',30,'normal','bold'))
            for i in circles:
                i.hideturtle()
                i.goto(0,400)
            circles = []
            amount = 5
            ammleft.clear()
            ammleft.write(f'You have {amount} ammo left')
            target.goto(random.randrange(-200,300),-95)

# Increases power by one
def increasepower():
    global power
    if ammo.launching == False:    
        if power < 10:
            power += 1
        powerlevel.clear()
        powerlevel.write(f'The power level is {power}')

# Decreases power by one
def decreasepower():
    global power,point
    if ammo.launching == False:
        if power > 1:
            power -= 1
        powerlevel.clear()
        powerlevel.write(f'The power level is {power}')

# Clears points of impact and sets ammo to 5
def reload():
    global circles,point,amount
    for i in circles:
        i.hideturtle()
        i.goto(0,400)
    circles = []
    amount = 5
    ammleft.clear()
    ammleft.write(f'You have {amount} ammo left')
    point = 0
    points.clear()
    points.write(point, font=('Arial',30,'normal','bold'))

# Allows input for player
bg.listen()
bg.onkeypress(launch,'space')
bg.onkeypress(turnright,'Right')
bg.onkeypress(turnleft,'Left')
bg.onkeypress(increasepower,'Up')
bg.onkeypress(decreasepower,'Down')
bg.onkeypress(reload,'r')

bg.mainloop()