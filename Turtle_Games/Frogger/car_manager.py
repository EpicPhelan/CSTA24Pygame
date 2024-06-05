from turtle import Turtle

from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.cars = []
        self.currentspeed = MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle()
        new_car.speed = self.currentspeed * (randint(50, 150) * 0.01)
        new_car.shape('square')
        new_car.shapesize(stretch_wid = 1, stretch_len = 2)
        #new_car.color(randint(0, 100) * 0.01, randint(0, 100) * 0.01, randint(0, 100) * 0.01)
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.goto(250, randint(-5, 5) * 20)
        self.cars.append(new_car)
    
    def go(self):
        for i in self.cars:
            newx = i.xcor() - i.speed
            i.goto(newx, i.ycor())
            if i.xcor() < -250:
                i.goto(250, randint(-5, 5) * 20)
                #i.color(randint(0, 100) * 0.01, randint(0, 100) * 0.01, randint(0, 100) * 0.01)
                i.color(choice(COLORS))
                i.speed = self.currentspeed * (randint(10, 200) * 0.01)
                
