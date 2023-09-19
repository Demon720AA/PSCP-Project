import pygame
from pygame.locals import *

# define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('Space Invaders')

# load image
background = pygame.image.load('graphics/background.jpg')

def draw_bg():
    screen.blit(background, (0, 0))
run = True
while run:
    
    clock.tick(fps)
    # draw brackground
    draw_bg()

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
