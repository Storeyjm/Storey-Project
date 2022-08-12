import imghdr
from pickle import TRUE
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
GOLD =  (255,215,  0)

map_1 =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,5,0,0,5,0,5,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,5,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,5,5,0,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,5,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
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
#End Class

# - Define class Enemy - Which is a sprite
class Enemy(pygame.sprite.Sprite):
    #Define constructor for Enemy
    def __init__(self, color, width, height, speed, x_pos, y_pos):
        #Set speed of the sprite
        self.speed = speed
        #Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos

    #End Procedure

    def update(self):
        if self.rect.y >= 0 and self.rect.y < screenHeight:
            self.rect.y = self.rect.y
        else:
            self.rect.y = 0
        #endif
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
        #Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #Set the positions of the attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class

### -- Game Class Loop
class Game():
  ## -- GAME LOGIC
    def __init__(self):
        # Create the counter and score
        self.myscore = 100
        pygame.font.init()
        self.myfont = pygame.font.SysFont(None, 24)
        self.img = self.myfont.render(str(self.myscore), True, GREEN)
        self.count = 0
        self.clock_speed = 24
        # Create a list of induvidual sprites
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        
        #Create the players
        self.my_player = Player(WHITE, 20, 20, 0)
        self.player_group.add (self.my_player)
        self.all_sprites_group.add (self.my_player)

        # Create enemies
        # List of enemy starting positions
        enemy_positions =[[530,50],[230,20],[420,148]]
        self.enemy_group = pygame.sprite.Group()
        for pos in range (3):
            my_enemy = Enemy(RED,20,20,0,enemy_positions[pos][0], enemy_positions[pos][1])
            self.enemy_group.add(my_enemy)
            self.all_sprites_group.add(my_enemy)
        #Next pos
        #Allows arrows to be created by having a counter.
        self.number_of_arrows = 0
        
        # Create Obstacles
        #Create the obstacles on screen
        for x in range (48):
            for y in range(64):
                if map_1[x][y] == 1:
                    my_obstacle = Obstacle(GREY, 20, 20, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif map_1[x][y] ==2:
                    my_obstacle = Obstacle(GREEN, 40, 40, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif map_1[x][y] ==3:
                    my_obstacle = Obstacle(BROWN, 20, 60, y*20, x*20)
                    self.obstacle_group.add(my_obstacle)
                    self.all_sprites_group.add(my_obstacle)
                elif map_1[x][y] ==5:
                    my_coin = Obstacle(GOLD, 20, 20, y*20, x*20)
                    self.coin_group.add(my_coin)
                    self.all_sprites_group.add(my_coin)
                #End if
            #Next x
        #Next y
    #End of constructor
    
    def game_run(self):
        # Create an all sprites group for all sprites in the game
        self.all_sprites_group.update()

        # Check for any key input
        for event in pygame.event.get():
            # close the game
            if event.type == pygame.QUIT:
                return True
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
        #Next x

        arrow_hit_list = pygame.sprite.groupcollide(self.arrow_group,self.enemy_group, True, True)
        for b in arrow_hit_list:
            self.myscore = self.myscore + 5
        #Next b
        arrow_hit_list = pygame.sprite.groupcollide(self.arrow_group, self.obstacle_group, True, False)

        player_hit_list = pygame.sprite.groupcollide(self.player_group, self.enemy_group, False, True)
        #for p in player_hit_list:
            #self.lives = self.lives - 1
            #print("lives:", self.lives) 
        #Next p

        # Coin collection and addition to the score
        player_hit_list = pygame.sprite.groupcollide(self.player_group, self.coin_group, False, True)
        for c in player_hit_list:
            self.myscore = self.myscore + 10
        #Next c

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
        self.all_sprites_group.update()
    
        # -- Screen background is BLACK
        screen.fill (BLACK)

        # -- Draw here
        self.all_sprites_group.draw (screen)
        # Display counter on-screen
        screen.blit(self.img, (20, 20))

        if self.count > self.clock_speed:
            self.myscore = self.myscore - 1
            #score_display = ("score:" + myscore)
            self.img = self.myfont.render(str(self.myscore), True, GREEN)
            self.count = 0
        self.count = self.count + 1
        
        # -- Flip display to reveal new position of objects 
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(self.clock_speed)

    # end of game run function
#End Class

# Create new game object
my_game = Game()
#Game loop
while not done:

    # Run the game
    done = my_game.game_run()

#Endwhile - End of game loop



pygame.quit()