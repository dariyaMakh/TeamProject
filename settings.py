class Settings():
    def __init__(self):
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 153, 153)
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction 1(right) -1(left)
        self.fleet_direction = 1