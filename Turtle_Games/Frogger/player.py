from turtle import Turtle

from random import randint

STARTING_POSITION = (0, -123)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 150


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(stretch_wid = 0.75, stretch_len = 0.725)
        self.color(0, 0.25, 0)
        self.left(90)
        self.goto(STARTING_POSITION)
    def go(self):
        newy=self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newy)
    
    def detect_win(self):
        return self.ycor() >= FINISH_LINE_Y

    def restart(self):
        self.goto(STARTING_POSITION)