import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # game initialization and screen creation + added settings initialization
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship creation
    ship = Ship(screen)


# Main loop
    while True:
        # Keyboard and mouse events tracking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # For every loop display depicts
        screen.fill(ai_settings.bg_color)
        ship.blit()
        # Last depicted screen display
        pygame.display.flip()


run_game()