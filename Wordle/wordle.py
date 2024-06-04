# Doing wordl together

import pygame
import random

# Initialize the game
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

# make the title for the window
pygame.display.set_caption("Wordle Clone")

# Color Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
DARKGREY = (100, 100, 100)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Set up Font
font = pygame.font.Font(None, 80)

class Player:
    def __init__(self):
        self.guesses = 0
        self.cur_row = 0
        self.cur_col = 0
        self.letters_guessed = []
        self.all_words = []
        self.current_word = ""
        self.load_words()
        self.secret = random.choice(self.all_words)
        print(self.secret)

    def load_words(self):
        # Fix the path to where you need it
        with open('Wordle/wordlelist.txt', 'r') as f:
            data = f.readlines()
            # List comprehension that reads each line and strips the newline then adds theem to a list
            self.all_words = [line.strip("\n").upper() for line in data]
        
        
    def check_letters(self):
        if self.current_word == self.secret:
            # change all of them green
            print("You guessed it")
            for bl in Block.board[player.cur_row]:
                bl.color = GREEN
            
        elif self.current_word in self.all_words:
            # real word so change block colors and clear current word
            for letter in self.current_word:
                if letter in self.secret:
                    # this letter is in the word. now we need to find where
                    # find rfind index count
                    # first find out how many times the letter is in there
                    num = self.secret.count(letter)
                    if num == 1:
                        if self.secret.find(letter) == self.current_word.find(letter):
                            Block.board[player.cur_row][self.secret.find(letter)].color = GREEN
                        else:
                            Block.board[player.cur_row][player.current_word.find(letter)].color = YELLOW
                    
                    if num == 2:
                        if self.secret.find(letter) == self.current_word.find(letter):
                            # first same letter on left
                            Block.board[player.cur_row][self.secret.find(letter)].color = GREEN
                        else:
                            Block.board[player.cur_row][player.current_word.find(letter)].color = YELLOW
                            
                        if self.secret.rfind(letter) == self.current_word.rfind(letter):
                            Block.board[player.cur_row][self.secret.rfind(letter)].color = GREEN
                        else:
                            Block.board[player.cur_row][player.current_word.rfind(letter)].color = YELLOW
                        
                    if num == 3:
                        print("Restart game")
                        
            self.current_word = ""       
            return True  
        else:
            return False

class Block:
    # this class variable stores the squares of guesses
    board = [[],[],[],[],[],[]]
    # Same thing, but with comprehension
    board = [[] for i in range(6)]
    
    #for i in range(6):
        #board.append([])
    
    # We need another board to keep track of the letters so we can iterate over them
    alpha_board = []
    
    def __init__(self, row, column, x, y, color, letter):
        self.x = x
        self.y = y
        self.color = color
        self.letter = letter
        self.row = row
        self.column = column
        
    def update(self):
        if self.letter == "ENTER":
            # If the button is the enter button we make it 200 wide
            pygame.draw.rect(screen, self.color, (self.x, self.y, 200, 50))
        else:
            # Otherwise each button is 50 x 50
            pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))
        # draw the letter on the rect
        txt = font.render(self.letter, True, DARKGREY)
        screen.blit(txt, (self.x , self.y))
    
    def clicked(self):
        ''' Detect if the mouse position is inside the box then play that letter '''
        mouse_pos = pygame.mouse.get_pos()
        # this is a tuple (mouseX, mouseY)
        if self.x < mouse_pos[0] < self.x + 50 and self.y < mouse_pos[1] < self.y + 50:
            print(f"{self.letter} pressed")
            
            # go to the current guess row and current guess column block and change it's letter
            if self.letter == "<" and player.cur_col > 0:
                Block.board[player.cur_row][player.cur_col - 1].letter = ""
                player.current_word = player.current_word[:-1]
                player.cur_col -= 1
            elif self.letter == "ENTER" and player.cur_col == 5:
                print(f"Player Guessed this word {player.current_word}")
                if player.check_letters():
                    player.cur_row += 1
                    player.cur_col = 0
                else:
                    print("wrong")
            elif player.cur_col < 5 and self.letter != "<" and self.letter != "ENTER":
                Block.board[player.cur_row][player.cur_col].letter = self.letter
                player.current_word += Block.board[player.cur_row][player.cur_col].letter
                player.cur_col += 1
            else:
                print("Out of room")
    
    # We encasulate this method in the class to so it can access the Block.board list 
    # Static methods don't take self as an argument and need a decorator to declare them 
    @staticmethod   
    def set_up_board():
        start_x = 100
        start_y = -20
        for row in range(6):
            start_y += 55
            for column in range(5):
                start_x += 55
                bl = Block(row, column, start_x, start_y, WHITE, "")
                Block.board[row].append(bl)
            start_x = 100
        
        # Set up the alphabet buttons
        # for the numbers 65 to 91 add the chr() of each number to our list alphabet
        alphabet = [chr(i) for i in range(65, 91)]
        start_x = -10
        for i in range(3):
            start_y += 55
            for j in range(9):
                start_x += 55
                if len(alphabet) == 0:
                    # this is where we add backspace and enter
                    alphbl = Block(i, j, start_x, start_y, GREY, "<")
                    Block.alpha_board.append(alphbl)
                    alphbl = Block(i, j, 200, start_y + 55, GREY, "ENTER")
                    Block.alpha_board.append(alphbl)
                else:
                    alphbl = Block(i, j, start_x, start_y, GREY, alphabet.pop(0))
                    # We store them into the Class variable list alphabet blocks
                    # this saves them from being overwritten
                    Block.alpha_board.append(alphbl)
            start_x = -10

# Instantiate Our Objects from our Classes    
player = Player()    

Block.set_up_board()

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for block in Block.alpha_board:
                block.clicked()

    # Update the screen to show the changes
    for row in Block.board:
        for block in row:
            block.update()
    for block in Block.alpha_board:
        block.update()
        
        
        
    pygame.display.flip()