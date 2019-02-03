import pygame


class Ship():
    def __init__(self, screen):
        # Initializes ship and sets its initial position
        self.screen = screen

        # Ship downloading and getting rectangle
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ship appears in bottom
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

    def blit(self):
        # pictures ship in current position
        self.screen.blit(self.image, self.rect)