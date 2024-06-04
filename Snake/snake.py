""" Snake Game with Pygame
Modified from https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

collide_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

# Snake
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = 'right'
        self.pos = [200,200]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], 10, 10)
        self.body = [[200,200], [180,200], [160,200]]
        
        
    def update(self):
        # Input Handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        if keys[pygame.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'
        if keys[pygame.K_UP] and self.direction != 'down':
            self.direction = 'up'
        if keys[pygame.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
            
        # Movement
        x,y = self.body[0]
        if self.direction == 'right':
            self.pos[0] += 10
        if self.direction == 'left':
            self.pos[0] -= 10
        if self.direction == 'up':
            self.pos[1] -= 10
        if self.direction == 'down':
            self.pos[1] += 10
        
        # Update body
        self.body.insert(0, list(self.pos))
        # remove last block
        self.body.pop()
        
        # Check collision with fruit with sprite collision
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], 10, 10)
        fruit_collision = pygame.sprite.spritecollide(self, collide_group, False)
        if fruit_collision:
            self.body.append(self.body[-1])
            fruit.move()
        
        # Check collision with wall
        wall_collision = pygame.sprite.spritecollide(self, wall_group, False)
        if wall_collision:
            print("Game Over")
            pygame.quit()
       
        
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.rect.Rect(segment[0], segment[1], 10, 10))

#MARK: FRUIT
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = [random.randint(100, 500), random.randint(100, 500)]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], 10, 10)
        collide_group.add(self)
        
        
    def draw(self):
        pygame.draw.rect(screen, RED, pygame.rect.Rect(self.pos[0], self.pos[1], 10, 10))
        
    def move(self):
        self.pos = [random.randint(100, 500), random.randint(100, 500)]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], 10, 10)
    
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.rect.Rect(x, y, width, height)
        wall_group.add(self)
    
    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)
    
#Mark: Objects       
player = Snake()          
fruit = Fruit()
left_wall = Wall(50, 50, 10, 500)
right_wall = Wall(600, 50, 10, 500)
top_wall = Wall(50, 50, 550, 10)
bottom_wall = Wall(50, 550, 560, 10)




#MARK: Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    
    # fill with light green
    screen.fill((144, 238, 144))
    player.update()
    player.draw()
    left_wall.draw()
    right_wall.draw()
    top_wall.draw()
    bottom_wall.draw()
    
    fruit.draw()
    
    # Display Score
    score_text = font.render(f"Score: {len(player.body) - 2}", True, BLACK)
    # Draw text
    screen.blit(score_text, (10, 10))
    
    
    pygame.display.flip()
    clock.tick(FPS)
    