from turtle import Turtle
import random

#draws board
lines = Turtle()

class Racer(Turtle):
    #class attribute to keep track of racers
    racers = []
    racing = True
    
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color(color)
        self.spd = random.randint(10,16)
        self.luck = random.randint(1,11)
        self.money = 100
        self.shape('turtle')
        self.penup()
        Racer.racers.append(self)

    def __str__(self):
        return self.name
        
    #new method to move
    def go(self, distance):
        self.forward(random.randint(1,distance) + (self.spd//5) + (self.luck//2))

    
def draw_lines():
    #start line
    lines.pu()
    lines.goto(-200, -100)
    lines.pd()
    lines.left(90)
    lines.forward(200)
    lines.pu()
    #finish line
    lines.goto(200,-100)
    lines.pd()
    lines.forward(200)
    lines.pu()
    lines.hideturtle()

draw_lines()

#Create your racers
terry = Racer("Terry", "red")
john = Racer("John", "blue")
eric = Racer("Eric", "orange")
gil = Racer("Gill", "yellow")
michael = Racer("Michael", "purple")

def start():
    #Place them on the starting line
    yPos = -100
    for turtle in Racer.racers:
        turtle.goto(-200, yPos)
        yPos += 50

start()

def race():
    #using our class attribute to control if we are racing or not
    while Racer.racing == True:
        for turtle in Racer.racers:
            turtle.go(3)
            if turtle.xcor() > 200:
                Racer.racing = False
                turtle.money += 50
                print(f'{turtle.name} Wins the Race!')
                return turtle

def main():
    print("Welcome to Turtle Racing!")
    print("These are your racers")
    for num, turt in enumerate(Racer.racers):
        print(f'{num} - {turt}')

    player_turtle = None
    while player_turtle == None:
        print("Who do you want to bet on?")
        bet = input()
        for turtle in Racer.racers:
            if bet.title() == turtle.name:
                player_turtle = turtle
                break
        else:
            print("Invalid Turtle")

    if player_turtle == race():
        print("You picked the winning turtle!")
    else:
        print("You did not pick the winning turtle")
main()
    

