# pygame boiler plate
import pygame
import random
# Initialize the pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((600, 600))
# Title 
pygame.display.set_caption("Dudey Jump")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (100, 100, 100)
YELLOW = (255, 255, 0)


    
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
        self.xvel = 0
        self.yvel = 0
        self.alive = True
        
    def update(self):
        # Gravity
        if self.alive:
            if self.yvel < 16:
                self.yvel += 1
            # Move the player
            self.rect.x += self.xvel
            self.rect.y += self.yvel
        
        # Lets player wrap around the screen
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 800
            
        # if player falls off bottom
        if self.rect.y > 600:
            self.alive = False
            self.rect.y = 600

        col = pygame.sprite.spritecollide(self, Platform.plats, False)
        if col:
            for plat in col:
                if plat.hit == False and self.yvel > 0:
                    self.yvel = -20
                    plat.hit = True
        
        floorcol = pygame.sprite.spritecollide(self, Floor.floor, False)
        if floorcol:
            self.yvel = -20
        
        # draw the player
        screen.blit(self.image, self.rect)
        
class Platform(pygame.sprite.Sprite):
    plats = pygame.sprite.Group()
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 550)
        self.rect.y = 0
        self.hit = False
        Platform.plats.add(self)
        
    def update(self):
        if player.alive:
        # check if the platform is hit
            if self.hit == False:
                self.image.fill(BLUE)
            else:
                self.image.fill(DARKGREY)
            
            # drop the platform
            self.rect.y += 3
            
            # check if the platform is off the screen
            if self.rect.top > 600:
                Platform.plats.remove(self)
                self.kill()
            
            # draw the platform
            screen.blit(self.image, self.rect)

class Floor(pygame.sprite.Sprite):
    floor = pygame.sprite.Group()
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((600, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 550
        screen.blit(self.image, self.rect)
        self.start_game = True
        self.timer = pygame.time.get_ticks()
        Floor.floor.add(self)

    def update(self):
        if self.start_game:
            if pygame.time.get_ticks() - self.timer > 5000:
                self.start_game = False
        if self.start_game:
            self.image.fill(GREEN)
            screen.blit(self.image, self.rect)
        else:
            self.rect.y = 1000
        

# Create objects
player = player()
floor = Floor()

# Create the start platforms
firstplat = Platform()
firstplat.rect.y = 200

secondplat = Platform()
secondplat.rect.y = 0
secondplat.rect.x = 250

thirdplat = Platform()
thirdplat.rect.y = -200
thirdplat.rect.x = 200
# Game Loop
running = True
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.xvel = -8
            if event.key == pygame.K_RIGHT:
                player.xvel = 8
    
    # Spawn the platforms
    if len(Platform.plats) < 5:
        newplat = Platform()
        
    
    # Fill the background to cover up the old drawings
    screen.fill(WHITE)
    # Update the shapes and sprites
    # Draw the shapes and sprites
    player.update()
    floor.update()
    
    for plat in Platform.plats:
        plat.update()
    
    
    # Update the display
    pygame.display.flip()
    # Tick the clock to control FPS
    clock.tick(FPS)
    