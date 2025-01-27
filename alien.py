import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # a class to represent a single alien in a fleet.

    def __init__(self, ai_game):
        # initialize the alien and set its starting position.
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect attribute.
        self.image = pygame.image.load('image/alien.bmp')  
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position.
        self.x = float(self.rect.x)