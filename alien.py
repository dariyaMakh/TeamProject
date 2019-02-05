import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Download alien image and rect attribute assignment
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        # every new alien appears on the bottom left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # saving actual alien position
        self.x = float(self.rect.x)

    def blit(self):
        # outputs alien in actual position
        self.screen.blit(self.image, self.rect)