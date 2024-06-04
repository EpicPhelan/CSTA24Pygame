""" 
Pygame is a game library made for python. 
There a built in classes and functions that let us move objects around the screen,

to install pygame:
we use the community edition of pygame, which is a fork of the original pygame library
pip install pygame-ce

"""


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window all caps means it's a constant
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# this makes the text on the window
pygame.display.set_caption("Hangman Game")
# Draw text Hangman at the top
# This makes the font that we can then put on the screen
# This is the font object, if you put None it defaults to the system font
font = pygame.font.Font("freesansbold.ttf", 40)
# this turns the font into pixels
text = font.render("Hangman", True, (0,0,0))

class Player():
    def __init__(self, guesses: str, wrong_guesses: int, word: str):
        self.guesses = guesses
        self.wrong_guesses = wrong_guesses
        self.word = word
        # this is an example encapsulation
        self.__letters = "abcdefghijklmnopqrstuvwxyz"
    
    def guess_letter(self, letter: str) -> None:
        ''' takes a string letter and adds it to the guesses string'''
        # we build the string guesses by concatenating the strings
        # guesses is not changed in place, it's a new string
        if letter not in self.guesses:
            self.guesses += letter
            # the replace method will find the first occurance of the letter and replace it with the second argument
            self.__letters = self.__letters.replace(letter, "")
            if letter not in self.word:
                self.wrong_guesses += 1
                print(f"Wrong guesses: {self.wrong_guesses}")
            else:
                print(f"{letter} is in the word {self.guesses}")
                for i in range(len(self.word)):
                    if self.word[i] in self.guesses:
                        if i == len(self.word) - 1:
                            print("You win")
                        else:
                            continue
                    else:
                        break
                
        else:
            print(f"You already guessed {letter} {self.guesses}")
            
        if self.wrong_guesses >= 6:
            print(f"You lose the word was {self.word}")
            # end the game
            pygame.quit()
        
    def show_letters_remaining(self):
        ''' Show the letters remaining on the screen '''
        text = font.render(self.__letters, True, (0,0,0))
        window.blit(text, (200, 500))   
            
    def update_spaces(self):
        start_x = 300
        spacing = 50
        """ Draws empty spaces and fills them in with correct letters """ 
        for num, letter in enumerate(self.word):
            if letter in self.guesses:
                # I thought the 10 was the font size but it is 
                # the background color. That's why they were black
                # This is wrong                           
                #txt = font.render(letter, False, (0,0,0), 10)
                # This is correct
                txt = font.render(letter, False, (0,0,0))
                window.blit(txt, (start_x, 200))
        
            else:
                dashtxt = font.render("_", False, (0,0,0))
                window.blit(dashtxt, (start_x, 200))
            start_x += spacing
                
        
    def update_stickman(self):
        # draw stick person
        if self.wrong_guesses >= 1:
            # head is circle             color    x   y  radius  width
            pygame.draw.circle(window, (0,0,0), (200, 175), 25, 2)
        if self.wrong_guesses >= 2:
            # body is a line
            pygame.draw.line(window, (0,0,0), (200, 200), (200, 300), 2)
        if self.wrong_guesses >= 3:
            # left arm
            pygame.draw.line(window, (0,0,0), (200, 225), (150, 250), 2)
        if self.wrong_guesses >= 4:
            # right arm
            pygame.draw.line(window, (0,0,0), (200, 225), (250, 250), 2)
        if self.wrong_guesses >= 5:# left leg
            pygame.draw.line(window, (0,0,0), (200, 300), (150, 350), 2)
        if self.wrong_guesses >= 6:
            # right leg
            pygame.draw.line(window, (0,0,0), (200, 300), (250, 350), 2)

def add_words_to_words():
    """ Adds words to the words list """
    with open("Hangman/wordlist.txt", "r") as file:
        # we need to get the words out into a list
        temp_list = file.readlines()
        # Time to get rid of the newline characters
        # we use a list comprehension to do this
        temp_2 = [word.strip('\n') for word in temp_list]
        
        # Make a list with words between 4 and 9 characters
        #temp_3 = [word for word in temp_2 if len(word)> 3 and len(word) < 10]
        temp_3 = []
        for word in temp_2:
            if len(word) > 3 and len(word) < 10:
                temp_3.append(word)
        return temp_3
# call it to make sure it works    


# Game variables
words = add_words_to_words()
word = random.choice(words)  # The word to guess
player = Player("", 0, word)



# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # check for q button being pressed to quit
            letter = chr(event.key)
            player.guess_letter(letter)
            

    # fills it with a color in an RGB Tuple
    window.fill((200, 200, 200))
    
    # This draws the text on the screen
    window.blit(text, (WINDOW_WIDTH // 2 - 50, 20))

    # Draw the gallows pole
    # pygame draw module will draw simple shapes
    # lines are drawn on the window, color, start point xy and end point xy, and width
    pygame.draw.line(window, (0,0,0), (100,400), (100,100), 8)
    pygame.draw.line(window, (0,0,0), (100,100), (200,100), 8)
    pygame.draw.line(window, (0,0,0), (200,100), (200,150), 4)
    
    player.update_spaces()
    player.update_stickman()
    player.show_letters_remaining()
    
    
    
    
    
    
    # Update the display
    pygame.display.update()
    pygame.display.flip()
    
    

# Quit the game
pygame.quit()