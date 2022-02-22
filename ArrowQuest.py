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
screenHeight = 480
screenWidth = 640
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
        self.rect.y = screenHeight - height
        self.rect.x = (screenWidth - width) / 2
        self.Vspeed = 0
        self.Hspeed = 0
    #End Procedure

    def update(self):
        if self.rect.x < 0 or self.rect.x > 600:
            if self.rect.x > 600:
                self.rect.x = 600
            elif self.rect.x < 0:
                self.rect.x = 0
        else:
            self.rect.x = self.rect.x + self.Hspeed
            #End if
        #End if
        if self.rect.y < 0 or self.rect.y > 450:
            if self.rect.y > 450:
                self.rect.y = 450
            elif self.rect.y < 0:
                self.rect.y = 0
            #End if
        else:
            self.rect.y = self.rect.y + self.Vspeed
        #End if
    #End function
#End Class

# - Define class Enemy - Which is a sprite
class Enemy(pygame.sprite.Sprite):
    #Define constructor for Snow
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

class arrow(pygame.sprite.Sprite):
    # Define constructor for Player
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

### -- Game Class Loop
class Game():
  ## -- GAME LOGIC
    def __init__(self):
        # Create a list of induvidual sprites
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        
        #Create the players
        self.my_player = Player(WHITE, 30, 30, 0)
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
    # End of constructor
    
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
                if event.key == pygame.K_RIGHT:
                    self.my_player.Hspeed = 5
                    self.my_player.facing = 3
                #End if
            #End if
                #if the left arrow key is pressed, move left
                elif event.key == pygame.K_LEFT and self.my_player.rect.x > 0:
                    self.my_player.Hspeed =-5
                    self.my_player.facing = 2
                #End if
                #if the up arrow key is pressed, move upwards
                elif event.key == pygame.K_UP and self.my_player.rect.y > 0:
                    self.my_player.Vspeed = -5
                    self.my_player.facing = 0
                #End if
                 
                #if the down arrow key is pressed, move downwards
                elif event.key == pygame.K_DOWN and self.my_player.rect.y < screenHeight - 30:
                    self.my_player.Vspeed = 5
                    self.my_player.facing = 1
                #End if

                #if the spacebar is pressed, fire an arrow
                elif event.key == pygame.K_SPACE:
                    #Counter goes up whenever the spacebar is pressed
                    self.number_of_arrows = self.number_of_arrows + 1
                    #define attributes of arrow based on direction the player is facing
                    if self.my_player.facing == 0:
                        my_arrow = arrow(WHITE, 5, 10, self.my_player.rect.x + (self.my_player.width*0.5), self.my_player.rect.y, 0, -2)
                    elif self.my_player.facing == 1:
                        my_arrow = arrow(WHITE, 5, 10, self.my_player.rect.x + (self.my_player.width*0.5), self.my_player.rect.y + self.my_player.height, 0, 2)
                    elif self.my_player.facing == 2:
                        my_arrow = arrow(WHITE, 10, 5, self.my_player.rect.x, self.my_player.rect.y + (self.my_player.height*0.5), -2, 0)
                    elif self.my_player.facing == 3:
                        my_arrow = arrow(WHITE, 10, 5, self.my_player.rect.x + self.my_player.width, self.my_player.rect.y + (self.my_player.height*0.5), 2, 0)
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

        # -- Screen background is BLACK
        screen.fill (BLACK)

        # -- Draw here
        self.all_sprites_group.draw (screen)

        # -- Flip display to reveal new position of objects 
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)

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