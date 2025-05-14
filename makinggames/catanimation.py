import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

catx2 = 50
caty2 = 50
direction2 = 'left'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    if direction2 == 'left':
        catx2 -= 10
        if catx2 == 10:
            direction2 = 'down'
    elif direction2 == 'down':
        caty2 += 10
        if caty2 == 220:
            direction2 = 'right'
    elif direction2 == 'right':
        catx2 += 10
        if catx2 == 150:
            direction2 = 'up'
    elif direction2 == 'up':
        caty2 -= 10
        if caty2 == 10:
            direction2 = 'left'

    DISPLAYSURF.blit(catImg, (catx, caty))

    DISPLAYSURF.blit(catImg, (catx2, caty2))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)