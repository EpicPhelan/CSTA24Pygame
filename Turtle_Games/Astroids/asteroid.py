from turtle import Turtle
import random

class Asteroid(Turtle):
    asteroid_list = []
    # This gives us a dead zone of 40 pixels around (0,0)
    range_list = [(-290,-40), (40, 290)]
    
    
    def __init__(self, asize):
        super().__init__()
        self.asize = asize
        self.start_x = random.choice(Asteroid.range_list)
        self.start_y = random.choice(Asteroid.range_list)
        
        #set their direction
        self.setheading(random.randint(0,360))
        self.aspeed = 2
        
        #looks
        self.shapesize(stretch_len = asize, stretch_wid = asize)
        self.shape('square')
        self.color('grey')
        self.pu()
        
        
        #add themselves to the class list
        Asteroid.asteroid_list.append(self)
        
    def move(self):
        ''' Moves asteroid and wraps it around screen '''
        self.forward(self.aspeed)
        #wrap around
        if self.xcor() > 300:
            self.goto(-300, self.ycor())
        if self.xcor() < -300:
            self.goto(300, self.ycor())
            
        if self.ycor() > 300:
            self.goto(self.xcor(), -300)
        if self.ycor() < -300:
            self.goto(self.xcor(), 300)