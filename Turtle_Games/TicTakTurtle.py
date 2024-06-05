'''
Made by two of my students
Sarai and Quinn
Right Click or O and left click or X
'''
import turtle

tim = turtle.Turtle()
tim.speed(0)
#this turtle draws the board
tik_toe = turtle.Turtle()
tik_toe.speed(0)
#this turtle writes the win statement
bob = turtle.Turtle()
bob.speed(0)
bob.pencolor('green')
bob.pd()
#this allows the click assignment
window = turtle.Screen()
window.listen()

#tik tak toe board
def draw_board():
    tik_toe.pu()
    tik_toe.goto(-300,300)
    tik_toe.pensize(5)
    tik_toe.pd()
    #draws outer box shape
    for i in range(2):
        tik_toe.forward(600)
        tik_toe.right(90)
        tik_toe.forward(600)
        tik_toe.right(90)
    #draws inner boxes
    tik_toe.pu()
    tik_toe.goto(-100,300)
    tik_toe.pd()
    tik_toe.right(90)
    tik_toe.fd(600)
    tik_toe.pu()
    tik_toe.goto(100,300)
    tik_toe.pd()
    tik_toe.fd(600)
    tik_toe.pu()
    tik_toe.goto(-300,100)
    tik_toe.left(90)
    tik_toe.pd()
    tik_toe.fd(600)
    tik_toe.pu()
    tik_toe.goto(-300,-100)
    tik_toe.pd()
    tik_toe.fd(600)
    tik_toe.pu()
    tik_toe.hideturtle()
draw_board()

#function to draw X
def draw_x(x,y):
    if check(x,y,"X"):
        tim.pu()
        tim.goto(x-60,y-100)
        tim.pd()
        tim.color('red')
        tim.write("X",font=('Arial', 128,'normal','bold'))
#calls the win function to check for a win
        win("X")
#draws the X or O when player clicks
window.onclick(draw_x,1)

#function to draw O
def draw_o(x,y):
    if check(x,y,"O"):
        tim.pu()
        tim.goto(x-70,y-100)
        tim.pu()
        tim.color('blue')
        tim.write("O",font=('Arial', 128,'normal','bold'))
#calls the win function to check for a win
        win("O")
#draws the X or O when player clicks
window.onclick(draw_o,3)

#data structure for the board
#0s are false, 1s and 2s are True
board = [[0,0,0],[0,0,0],[0,0,0]]
#checking if each box has an 'X' or an 'O' in it
def check(x,y,xoro):
    #top left
    if x > -300 and x < -100:
        if y > 100 and y < 300:
            if board[0][0] == 0:
                board[0][0] = xoro
                return True
    #top middle
    if x > -100 and x < 100:
        if y > 100 and y < 300:
            if board[0][1] == 0:
                board[0][1] = xoro
                return True
    #top right
    if x > 100 and x < 300:
        if y > 100 and y < 300:
            if board[0][2] == 0:
                board[0][2] = xoro
                return True
    #middle left
    if x > -300 and x < -100:
        if y > -100 and y < 100:
            if board[1][0] == 0:
                board[1][0] = xoro
                return True
    #middle middle
    if x > -100 and x < 100:
        if y > -100 and y < 100:
            if board[1][1] == 0:
                board[1][1] = xoro
                return True
    #middle right
    if x > 100 and x < 300:
        if y > -100 and y < 100:
            if board[1][2] == 0:
                board[1][2] = xoro
                return True
    #bottom left
    if x > -300 and x < -100:
        if y > -300 and y < -100:
            if board[2][0] == 0:
                board[2][0] = xoro
                return True
    #bottom middle
    if x > -100 and x < 100:
        if y > -300 and y < -100:
            if board[2][1] == 0:
                board[2][1] = xoro
                return True
    #bottom right
    if x > 100 and x < 300:
        if y > -300 and y < -100:
            if board[2][2] == 0:
                board[2][2] = xoro
                return True

#checks for wins (3 in a row of either X or O)
def win(arg):
    #top row win
    if board[0][0] == arg:
        if board[0][1] == arg:
            if board[0][2] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
        
    #middle row win
    if board[1][0] == arg:
        if board[1][1] == arg:
            if board[1][2] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
                
    #bottom row win
    if board[2][0] == arg:
        if board[2][1] == arg:
            if board[2][2] == arg:
               bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
    
    #1 column win
    if board[0][0] == arg:
        if board[1][0] == arg:
            if board[2][0] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
        
    #2 column win
    if board[0][1] == arg:
        if board[1][1] == arg:
            if board[2][1] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
    
    #3 column win
    if board[0][2] == arg:
        if board[1][2] == arg:
            if board[2][2] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
    
    #top left to bottom right diagonal win
    if board[0][0] == arg:
        if board[1][1] == arg:
            if board[2][2] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
    
    #bottom left to top right diagonal win
    if board[2][0] == arg:
        if board[1][1] == arg:
            if board[0][2] == arg:
                bob.write(f"{arg}s won!",font=('Times New Roman', 50,'normal','bold'))
                
window.mainloop()