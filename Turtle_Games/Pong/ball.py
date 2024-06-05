from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        #custom attributes
        self.shape('square')
        self.color('white')
        self.penup()
        self.xmove = 5
        self.ymove = 5
    
    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x,new_y)
    def bounce(self):
        #inverts the y direction
        self.ymove = self.ymove * -1
    def hit(self):
        self.xmove = self.xmove * -1