from turtle import Turtle

#create a paddle subclass of Turtle
class Paddle(Turtle):
    def __init__(self,lor):
        #super is the Turtle class
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        if lor == "left":
            self.xval = -200
            self.goto(self.xval,0)
        elif lor == "right":
            self.xval = 200
            self.goto(self.xval,0)
    #Methods to move our object
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xval, new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xval, new_y)