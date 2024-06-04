# pygame boiler plate
import pygame
# Initialize the pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800, 600))
# Title 
pygame.display.set_caption("Pygame Game")
# Clock and FPS
clock = pygame.time.Clock()
FPS = 60
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
DARKGREY = (100, 100, 100)
YELLOW = (255, 255, 0)

# Create shapes or sprites
player = pygame.Rect(50, 50, 50, 50)

# Game Loop
running = True
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Check for key presses
            if event.key == pygame.K_LEFT:
                player.x -= 10
            if event.key == pygame.K_RIGHT:
                player.x += 10
            if event.key == pygame.K_UP:
                player.y -= 10
            if event.key == pygame.K_DOWN:
                player.y += 10
    # Fill the background to cover up the old drawings
    screen.fill(WHITE)
    # Update the shapes and sprites
    # Draw the shapes and sprites
    pygame.draw.rect(screen, BLACK, player)
    # Update the display
    pygame.display.flip()
    # Tick the clock to control FPS
    clock.tick(FPS)
    