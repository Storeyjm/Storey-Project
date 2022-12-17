import imghdr
from pickle import FALSE, TRUE
from tkinter import Y
import pygame
import random
import math

from pygame.display import update
# -- Global Constants

#Colours
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (255,  0,  0)
GREY =  (163,163,163)
GREEN = (151,244,139)
BROWN = (165, 42, 42)
L_BROWN=(160, 40, 40)
GOLD =  (255,215,  0)
BLUE =  (100,220,255)
ORANGE =(255,173, 26)
PINK =  (255,160,160)

map_1 =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,3,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,1,0,0,5,0,5,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,8,0,5,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,5,0,8,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,5,0,5,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,5,8,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,5,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,8,0,8,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,5,5,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,5,5,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,5,5,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,5,5,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,2,0,2,0,2,0,2,0,2,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,5,8,5,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,5,5,5,5,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,8,8,5,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,5,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,5,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,2,0,2,0,2,0,2,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_2 =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,5,0,0,5,0,5,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,5,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,5,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,7,7,7,7,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,7,7,7,7,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,6,6,6,6,6,6,6,0,5,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,6,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
map_block_size = 20

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
screenHeight = 960
screenWidth = 1280
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

#-- Title of new window/screen
pygame.display.set_caption("Arrow Quest")
background_img = pygame.image.load("Background.jpg").convert()

# -- Exit game flag set to false
done = False
 
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# - Define class Player - Which is a sprite
class Player(pygame.sprite.Sprite):
    # Define constructor for Player
    def __init__(self, color, width, height, facing_pos):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        self.facing = facing_pos
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = screenHeight - map_block_size - self.height
        self.rect.x = screenWidth / 2
        self.Vspeed = 0
        self.Hspeed = 0
    #End Procedure

    def update(self):
        if self.rect.x < map_block_size or self.rect.x > (screenWidth - map_block_size):
            if self.rect.x > (screenWidth - map_block_size):
                self.rect.x = (screenWidth - map_block_size - self.width)
            elif self.rect.x < map_block_size:
                self.rect.x = map_block_size
            #End if
        else:
            self.rect.x = self.rect.x + self.Hspeed
        #End if
        if self.rect.y < map_block_size or self.rect.y > screenHeight - map_block_size:
            if self.rect.y > screenHeight - map_block_size:
                self.rect.y = (screenHeight - map_block_size - self.height)
            elif self.rect.y < map_block_size:
                self.rect.y = map_block_size
            #End if
        else:
            self.rect.y = self.rect.y + self.Vspeed
        #End if
    #End function

    def get_x(self):
        return self.rect.x
    # end get

    def get_y(self):
        return self.rect.y
    # end get
#End Class

# - Define class Enemy - Which is a sprite
class Enemy(pygame.sprite.Sprite):
    #Define constructor for Enemy
    def __init__(self, color, width, height, speed, x_pos, y_pos, facing_pos, chasing):
        #Set speed of the sprite
        self.start_y = y_pos
        self.start_x = x_pos
        #Call the sprite constructor
        super().__init__()
        #self.image = pygame.image.load("Img/Enemy.png").convert
        #self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.facing = facing_pos
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos
        self.x_dist = 150
        self.y_dist = 100
        self.speed = speed
        self.x_speed = 0
        self.y_speed = 0
        self.curr_x = 0
        self.curr_y = 0
        self.old_x = 0
        self.old_y = 0
        # chasing the player when set to 1
        self.chasing = chasing
        self.enemy_flag = 0
    #End Procedure

    def set_enemy_flag(self,val):
        self.enemy_flag = val
    # end procedure

    def chase_player(self):
        play_x = my_game.my_player.get_x()
        play_y = my_game.my_player.get_y()
        
        x_diff = self.rect.x - play_x
        y_diff = self.rect.y - play_y

        if x_diff ==0:
            x_diff = 1
        if y_diff == 0:
            y_diff = 1

        
        if abs(y_diff) < abs(x_diff):
            move_x = abs(x_diff) // abs(y_diff)
            move_y = 1
        else:
            move_y = abs(y_diff) // abs(x_diff)
            move_x = 1
        #end if

        if x_diff > 0:
            move_x = move_x * -1
        #end if

        if y_diff > 0:
            move_y = move_y * -1
        #end if
       
        return move_x, move_y
        
    #end chase player function

    def check_line_of_sight(self):
        # get the ratio to the player
        x_speed, y_speed = self.chase_player()
        play_x = my_game.my_player.get_x()
        play_y = my_game.my_player.get_y()
        #los = line of sight. Make a copy of the postiion of the enemy. 
        los_pos_x = self.rect.x
        los_pos_y = self.rect.y
        curr_x = abs(x_speed)
        curr_y = abs(y_speed)
        while los_pos_x != play_x and los_pos_y != play_y:
            if curr_x >= curr_y:
                if curr_x < 0:
                    los_pos_x-= 1
                else:
                    los_pos_x+= 1
                #end if
                self.curr_x -= 1
            else:
                if self.y_speed < 0:
                    self.rect.y = self.rect.y - 1
                else:
                    self.rect.y += 1
                #end if
                self.curr_y -= 1
            # end if

    #### end check line of sight function   

    def update(self):
        if self.chasing == 0:
            # 0 is moving up and 1 is moving down 
            if self.facing == 0 or self.facing ==1:
                if self.rect.y >= self.start_y and self.rect.y <= self.start_y + self.y_dist:
                    self.rect.y = self.rect.y + self.speed
                else:
                    # change direction from down to up
                    if self.facing == 1:
                        self.speed = random.randrange(2,5) * -1
                        self.facing = 0
                        self.rect.y = self.rect.y + self.speed
                        # change direction from up to down
                    elif self.facing == 0:
                        self.facing = 1
                        self.speed = random.randrange(2,5)
                        self.y_dist = random.randrange(100,150)
                        self.rect.y = self.rect.y + self.speed
                    #endif
            # 2 is moving left and 3 is moving right
            elif self.facing == 2 or self.facing ==3:
                if self.rect.x >= self.start_x and self.rect.x <= self.start_x + self.x_dist:
                    self.rect.x = self.rect.x + self.speed
                else:
                    #change direction from left to right
                    if self.facing == 2:
                        self.facing = 3
                        self.speed = random.randrange(2,5) * -1
                        self.rect.x = self.rect.x + self.speed
                    #change direction from right to left
                    elif self.facing == 3:
                        self.facing = 2
                        self.speed = random.randrange(2,5)
                        self.x_dist = random.randrange(150,200)
                        self.rect.x = self.rect.x + self.speed
                    #endif
                #endif
            #endif
        else:
            # Enemy is chasing the player
            #line_of_sight = self.check_line_of_sight()
            if self.enemy_flag == 0:
                self.x_speed, self.y_speed = self.chase_player()
                self.curr_x = abs(self.x_speed)
                self.curr_y = abs(self.y_speed)
                self.enemy_flag = self.enemy_flag + 1
            # This sets the amount of time before the enemy re-evaluates the position of the player
            elif self.enemy_flag < 10:
                if self.curr_x == 0 and self.curr_y == 0:
                    self.curr_x = abs(self.x_speed)
                    self.curr_y = abs(self.y_speed)
                else:
                    if self.curr_x >= self.curr_y:
                        if self.x_speed < 0:
                            self.old_x = self.rect.x
                            self.rect.x -= 1
                        else:
                            self.old_x = self.rect.x
                            self.rect.x += 1
                        #end if
                        self.curr_x -= 1
                    else:
                        if self.y_speed < 0:
                            self.old_y = self.rect.y
                            self.rect.y = self.rect.y - 1
                        else:
                            self.old_y = self.rect.y
                            self.rect.y += 1
                        #end if
                        self.curr_y -= 1
                    # end if
                self.enemy_flag = self.enemy_flag + 1
            else:
                self.enemy_flag = 0
            #endif
        #end if
    #End Procedure
#End Class

#Define class Arrow, which is a Sprite
class arrow(pygame.sprite.Sprite):
    # Define constructor for Arrow
    def __init__(self, color, width, height, x_pos, y_pos, x_speed, y_speed):
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = y_pos - height
        self.rect.x = x_pos
    #End Procedure
    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
        #endif 
    #End Procedure
#End Class

#Define class Obstacle, which is a sprite
class Obstacle(pygame.sprite.Sprite):
    #Define the constructor for the Sprite
    def __init__(self, color, width, height, x_ref, y_ref):
        #Call the sprite constructor
        super().__init__()
        #boulder_icon.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        #tree_icon.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        #Create a sprite and fill it with color
       
        if color==GREY:
            self.image = pygame.image.load("Boulder.jpg").convert()
            self.rect = self.image.get_rect()
            self.image.set_colorkey(BLACK)
        elif color == GOLD:
            self.image = pygame.image.load("5_coin.jpg").convert()
            self.rect = self.image.get_rect()
        elif color == ORANGE:
            self.image = pygame.image.load("10_coin.jpg").convert()
            self.rect = self.image.get_rect()
        elif color == L_BROWN:
            self.image = pygame.image.load("Bridge.jpg").convert()
            self.rect = self.image.get_rect()
        elif color == BROWN:
            self.image = pygame.image.load("Tree.jpg").convert()
            self.rect = self.image.get_rect()
            self.image.set_colorkey(BLACK)
        elif color == PINK:
            self.image = pygame.image.load("Goal.jpg").convert()
            self.rect = self.image.get_rect()
        elif color == GREEN:
            self.image = pygame.image.load("Bush.jpg").convert()
            self.rect = self.image.get_rect()
            self.image.set_colorkey(BLACK)
        else:
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.image.fill(color)
        #End if

        #Set the positions of the attributes
        self.rect.y = y_ref
        self.rect.x = x_ref
    #End Procedure
#End Class

### -- Game Class Loop
class Game():
  ## -- GAME LOGIC
    def __init__(self,level):
        if level == 1:
            current_map = map_1
            enemy_range = 6
        elif level == 2:
            current_map = map_2
            enemy_range = 5
        #end if

        # Create the counter and score and reset the coin counter for the start of the game
        self.myscore = 100
        self.mylives = 3
        self.mycoincounter = 0
        self.level = level
        pygame.font.init()
        self.myfont = pygame.font.SysFont(None, 24)
        self.score_img = self.myfont.render("Score: " + str(self.myscore), True, GREEN)
        self.lives_img = self.myfont.render("Lives: " + str(self.mylives), True, RED)
        self.count = 0
        self.clock_speed = 24
        # Create a list of induvidual sprites
        self.arrow_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.ten_coin_group = pygame.sprite.Group
        self.goal_group = pygame.sprite.Group()
        self.bridge_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        # Create player_group after other objects to ensure that the player is always seen
        self.player_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()


        #Allows arrows to be created by having a counter.
        self.number_of_arrows = 0
        
        # Create Obstacles
        #Create the obstacles on screen
        for x in range (48):
            for y in range(64):
                if current_map[x][y] == 1:
                    my_obstacle = Obstacle(GREY, 20, 20, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif current_map[x][y] ==2:
                    my_obstacle = Obstacle(GREEN, 40, 40, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif current_map[x][y] ==3:
                    my_obstacle = Obstacle(BROWN, 20, 60, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif current_map[x][y] ==4:
                    my_goal = Obstacle(PINK, 20, 20, y*20, x*20)
                    self.goal_group.add(my_goal)
                    self.all_sprites_group.add(my_goal)
                elif current_map[x][y] ==5:
                    my_coin = Obstacle(GOLD, 20, 20, y*20, x*20)
                    self.coin_group.add(my_coin)
                    self.all_sprites_group.add(my_coin)
                elif current_map[x][y] ==6:
                    my_obstacle = Obstacle(BLUE, 20, 20, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif current_map[x][y] ==7:
                    my_bridge = Obstacle(L_BROWN, 20, 20, y*20, x*20)
                    self.bridge_group.add(my_bridge)
                    self.all_sprites_group.add(my_bridge)
                elif current_map[x][y] ==8:
                    my_ten_coin = Obstacle(ORANGE, 20, 20, y*20, x*20)
                    self.ten_coin_group.add(my_ten_coin)
                    self.all_sprites_group.add(my_ten_coin)
                #End if
            #Next x
        #Next y
        
        # Create enemies after obstacles so they appear in front
        # List of enemy starting positions and facing directions
        enemy_positions =[[580,340,1,1],[460,420,1,1],[400,200,1,0],[1100,380,1,0],[100,60,3,0],[520,780,3,0]]
        self.enemy_group = pygame.sprite.Group()
        for pos in range (enemy_range):
            my_enemy = Enemy(RED,20,20,3,enemy_positions[pos][0], enemy_positions[pos][1], enemy_positions[pos][2], enemy_positions[pos][3])
            self.enemy_group.add(my_enemy)
            self.all_sprites_group.add(my_enemy)
        #Next pos

        # Create the players after all other objects so it can always be seen
        self.my_player = Player(WHITE, 20, 20, 0)
        self.player_group.add (self.my_player)
        self.all_sprites_group.add (self.my_player)
    #End of constructor
    
    def game_run(self):

        # Create an all sprites group for all sprites in the game
        self.all_sprites_group.update()

        # Check for any key input
        for event in pygame.event.get():
            # close the game
            if event.type == pygame.QUIT:
                self.level = 4
            #End if
            if event.type == pygame.KEYDOWN:
                #if the right arrow key is pressed, move right
                if event.key == pygame.K_RIGHT and self.my_player.rect.x < screenWidth - map_block_size:
                    self.my_player.Hspeed = map_block_size /4
                    self.my_player.facing = 3
                #End if
                #if the left arrow key is pressed, move left
                elif event.key == pygame.K_LEFT and self.my_player.rect.x > map_block_size:
                    self.my_player.Hspeed = -map_block_size /4
                    self.my_player.facing = 2
                #End if
                #if the up arrow key is pressed, move upwards
                elif event.key == pygame.K_UP and self.my_player.rect.y > map_block_size:
                    self.my_player.Vspeed = -map_block_size /4
                    self.my_player.facing = 0
                #End if
                 
                #if the down arrow key is pressed, move downwards
                elif event.key == pygame.K_DOWN and self.my_player.rect.y < screenHeight - map_block_size:
                    self.my_player.Vspeed = map_block_size /4
                    self.my_player.facing = 1
                #End if

                #if the spacebar is pressed, fire an arrow
                elif event.key == pygame.K_SPACE:
                    #Counter goes up whenever the spacebar is pressed
                    self.number_of_arrows = self.number_of_arrows + 1
                    #define attributes of arrow based on direction the player is facing
                    if self.my_player.facing == 0:
                        my_arrow = arrow(WHITE, 5, 10, self.my_player.rect.x + (self.my_player.width*0.5), self.my_player.rect.y, 0, (-map_block_size /4)-2)
                    elif self.my_player.facing == 1:
                        my_arrow = arrow(WHITE, 5, 10, self.my_player.rect.x + (self.my_player.width*0.5), self.my_player.rect.y + self.my_player.height, 0, (map_block_size /4)+2)
                    elif self.my_player.facing == 2:
                        my_arrow = arrow(WHITE, 10, 5, self.my_player.rect.x, self.my_player.rect.y + (self.my_player.height*0.5), -(map_block_size /4)-2, 0)
                    elif self.my_player.facing == 3:
                        my_arrow = arrow(WHITE, 10, 5, self.my_player.rect.x + self.my_player.width, self.my_player.rect.y + (self.my_player.height*0.5), (map_block_size /4)+2, 0)
                    #End if
                    self.arrow_group.add (my_arrow)
                    self.all_sprites_group.add (my_arrow)
                #End if

            elif event.type == pygame.KEYUP:
                #when key is lifted, stop moving. This allows for smooth movement of the player.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.my_player.Hspeed = 0
                    self.my_player.Vspeed = 0
                #End if
            #End if
        #Next event

        arrow_hit_list = pygame.sprite.groupcollide(self.arrow_group,self.enemy_group, True, True)
        for b in arrow_hit_list:
            self.myscore = self.myscore + 5
        #Next b
        
        arrow_hit_list = pygame.sprite.groupcollide(self.arrow_group, self.obstacle_group, True, False)

        player_hit_list = pygame.sprite.groupcollide(self.player_group, self.enemy_group, False, True)
        for p in player_hit_list:
            self.mylives = self.mylives - 1
        #Next p

        # Coin collection and addition to the score
        coin_hit_list = pygame.sprite.groupcollide(self.player_group, self.coin_group, False, True)
        for c in coin_hit_list:
            self.myscore = self.myscore + 10
            self.mycoincounter = self.mycoincounter + 1
        #Next c

        # Ten coin collection and addition to the score
        #ten_coin_hit_list = pygame.sprite.groupcollide(self.player_group, self.ten_coin_group, False, True)
        #for t in ten_coin_hit_list:
       #     self.myscore = self.myscore + 10
        #    self.mycoincounter = self.mycoincounter + 10
        #Next t

        # -- Check for collisions between player and obstacles
        player_hit_list = pygame.sprite.groupcollide(self.player_group, self.obstacle_group, False, False)
        for hit in player_hit_list:
            self.my_player.Hspeed = 0
            self.my_player.Vspeed = 0
            self.my_player.rect.x = self.player_old_x
            self.my_player.rect.y = self.player_old_y
        #Next hit
        self.player_old_x = self.my_player.rect.x
        self.player_old_y = self.my_player.rect.y

        goal_hit_list = pygame.sprite.groupcollide(self.player_group, self.goal_group, False, False)
        for g in goal_hit_list:
            self.level = self.level + 1
            return self.level
        # -- Check for collisions between enemy and obstacles
        enemy_hit_list = pygame.sprite.groupcollide(self.enemy_group, self.obstacle_group, False, False)
        for e in enemy_hit_list:
            e.set_enemy_flag(0)
            e.rect.x = e.old_x
            e.rect.y = e.old_y
        #Next hit

        self.all_sprites_group.update()

        # -- Screen background is BLACK
        screen.fill (BLACK)
        screen.blit(background_img,[0,0])

        # -- Draw here
        self.all_sprites_group.draw (screen)
        # Display counter on-screen
        screen.blit(self.score_img, (20, 20))
        screen.blit(self.lives_img, (20, 40))

        # - Updates the counters on-screen every clock tick
        if self.count > self.clock_speed:
            self.myscore = self.myscore - 1
            self.score_img = self.myfont.render("Score: " + str(self.myscore), True, GREEN)
            self.count = 0
            self.lives_img = self.myfont.render("Lives: " + str(self.mylives), True, RED)
        self.count = self.count + 1
        #if self.myscore < 90:
            #self.level = self.level + 1
        
        # -- Flip display to reveal new position of objects 
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(self.clock_speed)

        return self.level

    # end of game run function
#End Class

# Create new game object

curr_level = 1
my_game = Game(curr_level)
#Game loop
while not done:
    # Run the game
    level = my_game.game_run()
    if level > curr_level:
        if level > 2:
            done = True
        else:
            my_game = Game(level)
            curr_level = level
        #end if
    #end if
#Endwhile - End of game loop



pygame.quit()