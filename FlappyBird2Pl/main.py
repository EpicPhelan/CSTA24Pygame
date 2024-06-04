""" Two player flappy bird game """
import pygame
from sys import exit
import random
pygame.init()

clock = pygame.time.Clock()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 551

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#images
bird_images = [pygame.image.load("bird_down.png"),
               pygame.image.load("bird_mid.png"),
               pygame.image.load("bird_up.png")]
r_bird_images = [pygame.image.load("rbird_down.png").convert_alpha(),
               pygame.image.load("rbird_mid.png").convert_alpha(),
               pygame.image.load("rbird_up.png").convert_alpha()]

skyline = pygame.image.load("clouds.jpg")
#ground = pygame.image.load("ground.png")
pipe_bottom = pygame.image.load("pipe_bottom.png")
pipe_top = pygame.image.load("pipe_top.png")


#variables
scroll_speed = 1
bird_start_pos = (100, 250)
bscore = 0
rscore = 0
font = pygame.font.SysFont("Segoe", 26)
big_font = pygame.font.SysFont("impact", 40)
game_stopped = True


class Bird(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_pos
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True
        self.color = color

    def update(self, user_input):
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        if self.color == "blue":
            self.image = bird_images[self.image_index // 10]
        else:
            self.image = r_bird_images[self.image_index // 10]

        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 560:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        if self.color == "blue":
            if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
                self.flap = True
                self.vel = -7
        if self.color == "red":
            if user_input[pygame.K_RALT] and not self.flap and self.rect.y > 0 and self.alive:
                self.flap = True
                self.vel = -7
        
    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= -self.image.get_width():
            self.kill()

        global bscore
        if self.pipe_type == "bottom":
            if bird_start_pos[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_pos[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                bscore += 1
        global rscore
        if self.pipe_type == "bottom":
            if bird_start_pos[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_pos[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                rscore += 1




def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                                     
def main():

    global bscore
    global rscore

    #bird = pygame.sprite.GroupSingle()
    #bird.add(Bird())
    bird = Bird("blue")
    rbird = Bird("red")

    pipe_timer = 0
    pipes = pygame.sprite.Group()

    
    ground = pygame.Rect(0, 560, 551, 160)
    col = (0, 255, 150)

    

    run = True
    while run:

        quit_game()

        screen.fill((0, 0, 0))

        

        user_input = pygame.key.get_pressed()

        screen.blit(skyline, (0, 0))

        pygame.draw.rect(screen, col, ground)

        bird.draw(screen)
        rbird.draw(screen) 
        pipes.draw(screen) 
        
              

        if bird.alive and rbird.alive:
            pipes.update()
        bird.update(user_input)
        rbird.update(user_input)

        
        if rbird.alive:
            blue_collision_pipes = pygame.sprite.spritecollide(bird, pipes, False)
        

        if blue_collision_pipes or (bird.rect.y >= 560 and rbird.alive):
            bird.alive = False
            if bird.rect.y >= 560:
                end_text = big_font.render("GAME OVER, Red Wins", True, pygame.Color(255, 255, 255))
                screen.blit(end_text, (120, 240))
                return_text = font.render("R to start over", True, pygame.Color(255, 255, 255))
                screen.blit(return_text, (210, 290))
                if user_input[pygame.K_r]:
                    bscore = 0
                    break
        if bird.alive:    
            red_collision_pipes = pygame.sprite.spritecollide(rbird, pipes, False)

        if red_collision_pipes or (rbird.rect.y >= 560 and bird.alive):
            rbird.alive = False
            if rbird.rect.y >= 560:
                end_text = big_font.render("GAME OVER, Blue Wins", True, pygame.Color(255, 255, 255))
                screen.blit(end_text, (120, 240))
                return_text = font.render("R to start over", True, pygame.Color(255, 255, 255))
                screen.blit(return_text, (210, 290))
                if user_input[pygame.K_LALT] or user_input[pygame.K_RALT] or user_input[pygame.K_r]:
                    rscore = 0
                    break


        if pipe_timer <= 0 and bird.alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + pipe_bottom.get_height()
            pipes.add(Pipe(x_top, y_top, pipe_top, "top"))
            pipes.add(Pipe(x_bottom, y_bottom, pipe_bottom, "bottom"))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1


        clock.tick(60)

        pygame.display.update()


def menu():
    global game_stopped
    ground = pygame.Rect(0, 560, 551, 160)
    col = (0, 255, 150)

    while game_stopped:
        quit_game()
        
        screen.fill((0, 0, 0))
        
        screen.blit(skyline, (0,0))
        pygame.draw.rect(screen, col, ground)
        screen.blit(bird_images[0], (100, 250))
        start_text = big_font.render("Press Space To Start", True, pygame.Color(255, 255, 255))
        screen.blit(start_text, (180, 250))
    
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

menu()


