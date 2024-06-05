from turtle import Turtle
import math

class Ship(Turtle):
    
    def __init__(self, img):
        super().__init__()
        self.shape(img)
        self.color('white')
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.pu()
        self.xVel = 0
        self.yVel = 0
        self.setheading(0)
        self.direction = self.heading()
        
    def move(self):
        ''' moves the ship to it's location plus it's velocities '''
        self.goto(self.xcor() + self.xVel, self.ycor() + self.yVel)
        
        
        #wrap around
        if self.xcor() > 300:
            self.goto(-300, self.ycor())
        if self.xcor() < -300:
            self.goto(300, self.ycor())
            
        if self.ycor() > 300:
            self.goto(self.xcor(), -300)
        if self.ycor() < -300:
            self.goto(self.xcor(), 300)
    
    def turn_clock(self):
        ''' Get the heading then set the heading '''
        current_angle = self.heading()
        self.setheading(current_angle - 10)
        
    def turn_counter(self):
        ''' Get the heading then set the heading '''
        current_angle = self.heading()
        self.setheading(current_angle + 10)  
          
    def boost(self):
        ''' Gets the angle and uses trig to tell 
        us the x and y component of our change in velocity '''
        angle = self.heading()
        self.xVel += math.cos(math.radians(angle))
        self.yVel += math.sin(math.radians(angle))