from turtle import Turtle

from random import randint

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        
    def score(self):
        self.clear()
        self.goto(-200, 130)
        self.write(f"score: {self.level}", align = "left", font = FONT)
    def game_over(self):
        self.goto(0, 0,)
        self.write("Game Over", align = "center", font = FONT)
    def score_up(self):
        self.level += 1