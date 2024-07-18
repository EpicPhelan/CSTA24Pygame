'''
This game was created by Claude AI
It only took two reprompts for the AI to get it right.
'''

import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def reset_game():
    global paddle_x, ball, ball_speed_x, ball_speed_y, game_over

    paddle_x = (WINDOW_WIDTH - paddle_width) // 2
    ball = pygame.Rect(WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
    ball_speed_x = 5
    ball_speed_y = 5
    game_over = False

# Define game objects
paddle_width = 80
paddle_height = 10
paddle_x = (WINDOW_WIDTH - paddle_width) // 2
paddle_y = WINDOW_HEIGHT - paddle_height - 10
paddle_speed = 10

ball_radius = 10
ball = pygame.Rect(WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
ball_speed_x = 5
ball_speed_y = 5

# Bricks
brick_width = 60
brick_height = 20
brick_gap = 5
bricks = []
for row in range(5):
    for col in range(WINDOW_WIDTH // (brick_width + brick_gap)):
        x = col * (brick_width + brick_gap)
        y = row * (brick_height + brick_gap)
        bricks.append(pygame.Rect(x, y, brick_width, brick_height))

# Game loop
running = True
game_over = False
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                reset_game()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WINDOW_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with walls
    if ball.left <= 0 or ball.right >= WINDOW_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Check for collision with paddle
    if ball.bottom >= paddle_y and ball.right >= paddle_x and ball.left <= paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # Check for collision with bricks
    brick_hit = False
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            brick_hit = True
            break

    # Check for game over
    if ball.top > WINDOW_HEIGHT:
        game_over = True

    # Clear the window
    window.fill(BLACK)

    # Draw the paddle
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(window, WHITE, paddle)

    # Draw the ball
    pygame.draw.rect(window, RED, ball)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(window, WHITE, brick)

    # Game over message
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press Space to Restart", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()