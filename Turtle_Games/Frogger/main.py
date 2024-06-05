""" My Version of Angela Yu's frogger from 100 days of Python"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

carManager = CarManager()

sb = Scoreboard()
sb.score()

screen.onkey(player.go, 'Up')
screen.listen()

spawncarCD = 1
spawnCDTime = 0

maxCars = 10

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if spawnCDTime <= 0 and len(carManager.cars) < maxCars:
        carManager.create_car()
        spawnCDTime = spawncarCD
    else:
        spawnCDTime -= 1
    
    carManager.go()
    for i in carManager.cars:
        if player.xcor() <= i.xcor() + 24 and player.xcor() >= i.xcor() - 24 and player.ycor() <= i.ycor() + 10 and player.ycor() >= i.ycor() - 10:
            game_is_on = False
            sb.game_over()
    if player.detect_win():
        sb.score_up()
        sb.score()
        carManager.currentspeed += 5
        player.restart()
    screen.update()
