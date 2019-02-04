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
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

    def blit(self):
        # pictures ship in current position
        self.screen.blit(self.image, self.rect)