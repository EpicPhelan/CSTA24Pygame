'''From Angela Yu/'s 100 days of code'''
import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

bg = turtle.Screen()
bg.tracer(0) #turns off animation
bg.bgcolor('black')
#instantiate our objects from our Paddle class
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
sb = Scoreboard()
#How to detect keystrokes
bg.onkey(right_paddle.move_up,'Up')
bg.onkey(right_paddle.move_down,'Down')
bg.onkey(left_paddle.move_up,'w')
bg.onkey(left_paddle.move_down,'s')
bg.listen()

while True:
    time.sleep(.05)
    bg.update()
    ball.move()
    if ball.ycor() > 100 or ball.ycor() < -100:
        ball.bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 200:
        ball.hit()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -200:
        ball.hit()
    #detect wins
    if ball.xcor() > 220:
        ball.goto(0,0)
        sb.l_scores()
    if ball.xcor() < -220:
        ball.goto(0,0)
        sb.r_scores()
