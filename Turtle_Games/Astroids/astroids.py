'''
My classes try at making asteroids 
Big thanks to https://trinket.io/python/4fb8b43036

Classes:
Ship - it will move with xVel and yVel
    Hitting forward will add force in the direction it is facing
Bullets - start at ship and move in the direction of the ship
asteroids - float about randomly

Todo:
image for ship
what happens after collisions
'''

import turtle
import time
import random
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid


# screen object

wn = turtle.Screen()
wn.bgcolor('black')
wn.screensize(300, 300)


# Create objects

# can't rotate registered shapes, only built ins
xwing = Ship("triangle")

for i in range(5):
    asteroid = Asteroid(3)
    asteroid.goto(random.randrange(asteroid.start_x[0], asteroid.start_x[1]), random.randrange(asteroid.start_y[0], asteroid.start_y[1]))


turtle.onkeypress(xwing.turn_counter, 'a')
turtle.onkeypress(xwing.turn_clock, 'd')
turtle.onkeypress(xwing.boost, 'w')
# use a lambda to pass through the  ship heading
turtle.onkeypress(lambda: Bullet.shoot(xwing.heading()), 'space')


# hit detection function
def detect_hits():
    ''' Looks for hits between asteroids ships and bullets '''
    for ast in Asteroid.asteroid_list:
        for bul in Bullet.bullets:
            if ast.distance(bul) < (ast.asize * 10):
                # bullet hits asteroid
                print("bullet hits asteroid")
                # bullet needs to go back to ship
                # increase score by 1
                # Asteroid needs to shrink a size and make a new one
                # if asteroid is size 1 it needs to disapear
                
        if ast.distance(xwing) < (ast.asize * 10):
            # ship is hit, game over
            print("ship hits asteroid")
           
            # set high score

# Let's look at module name and bases
print(Ship.__name__)
print(Ship.__bases__)
print(Ship.__module__)
print(Ship.__dict__)
print(xwing.__dict__)

# Turns off animation
wn.tracer(0)
# Main event loop
wn.listen()
while True:
    time.sleep(.05)
    xwing.move()
    # shoots bullets if shoot is true
    # otherwise go back to ship
    for bullet in Bullet.bullets:
        if bullet.shoot:
            bullet.move()
        else:
            bullet.goto(xwing.xcor(), xwing.ycor())
    
    # move asteroids
    for ast in Asteroid.asteroid_list:
        ast.move()
    detect_hits()
    wn.update()
    
    