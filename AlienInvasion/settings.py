class Settings():
    '''Класс для хранения настроек Alien Invasion'''
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (220, 220, 220) # RGB
        self.ship_speed = 0.5
        
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3