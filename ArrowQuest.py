import pygame
import random
import math

from pygame.display import update
# -- Global Constants

#Colours
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

#-- Title of new window/screen
pygame.display.set_caption("Arrow Quest")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End if
#Endwhile - End of game loop

pygame.quit()