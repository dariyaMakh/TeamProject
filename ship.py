import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # Initializes ship and sets its initial position
        self.screen = screen

        self.ai_settings = ai_settings

        # Ship downloading and getting rectangle
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ship appears in bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Saving actual ship center coordinates
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blit(self):
        # pictures ship in current position
        self.screen.blit(self.image, self.rect)