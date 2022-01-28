#Project
import pygame
import random
import math

from pygame.display import update
# -- Global Constants


# -- Colours
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

#-- Title of new window/screen
pygame.display.set_caption("Project")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# - Define class Enemy - Which is a sprite
class Enemy(pygame.sprite.Sprite):
    # Define constructor for Snow
    def __init__(self, color, width, height, speed):
        # Set speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = height
        self.rect.x = random.randrange(0, 600)
    #End Procedure
    def update(self):
        if self.rect.y >= 0 and self.rect.y < 475:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = 0
        #endif
    #End Procedure
#End Class

# - Define class Player - Which is a sprite
class Player(pygame.sprite.Sprite):
    # Define constructor for Player
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = 440
        self.rect.x = 320
        self.player_speed = 0
    #End Procedure
    def update(self):
        if self.rect.x < 0 or self.rect.x > 600:
            if self.rect.x > 600:
                self.rect.x = 600
            elif self.rect.x < 0:
                self.rect.x = 0
        else:
            self.rect.x = self.rect.x + self.player_speed
            #End if
        #End if



    #End Procedure
#End Class

class arrow(pygame.sprite.Sprite):
    # Define constructor for Player
    def __init__(self, color, width, height, speed, x, y):
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = y - height
        self.rect.x = x
    #End Procedure
    def update(self):
        self.rect.y = self.rect.y - self.speed
  
        #endif 
    #End Procedure
#End Class

### -- Game Loop
class Game():
  ## -- GAME LOGIC

    def __init__(self):
        # Create the variables
        self.score = 0
        # Create a list of induvidual sprites
        self.enemy_group = pygame.sprite.Group()
        self.player_group =pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        
        #Create the players
        self.my_enemy = Enemy(RED, 20, 20, 4)
        self.enemy_group.add (self.my_enemy)
        self.all_sprites_group.add (self.my_enemy)

        #Create the players
        self.my_player = Player(WHITE, 40, 40)
        self.player_group.add (self.my_player)
        self.all_sprites_group.add (self.my_player)

        #Create the arrows
        self.number_of_arrows = 0

    # End of constructor
        
    def game_run(self):

        self.all_sprites_group.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.my_player.player_speed = 5
                #End if
            #End if

                elif event.key == pygame.K_LEFT and self.my_player.rect.x > 0:
                    self.my_player.player_speed =-5
                #End if

                elif event.key == pygame.K_UP:
                    self.number_of_arrows = self.number_of_arrows + 1
                    my_arrow = arrow(WHITE, 5, 10, 2, self.my_player.rect.x + (self.my_player.width*0.5), 480 - self.my_player.height)
                    self.arrow_group.add (my_arrow)
                    self.all_sprites_group.add (my_arrow)
                #End if
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    self.my_player.player_speed = 0
                #End if
            #End if
        #Next x

        arrow_hit_list = pygame.sprite.groupcollide(self.arrow_group,self.enemy_group, True, True)
        for b in arrow_hit_list:
            self.score = self.score + 1
            print ("score:", self.score)
        #Next b
        player_hit_list = pygame.sprite.groupcollide(self.player_group, self.enemy_group, False, True)
        for p in player_hit_list:
            self.lives = self.lives - 1
            print("lives:", self.lives)
        #Next p

        # -- Screen background is GREY

        screen.fill (BLACK)

        # -- Draw here
        self.all_sprites_group.draw (screen)
        # -- Flip display to reveal new position of objects 
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)

    # end of game run function
#End Class

g = Game()
while not done:

    ret = g.game_run()

    if ret == True:
        done = True
#Endwhile - End of game loop

pygame.quit()