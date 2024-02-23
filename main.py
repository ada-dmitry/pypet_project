import sys 
import pygame
from settings import Settings

class AlienInvasion():
    '''Класс всей игры'''

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # Поменять разрешение
        self.screen = pygame.display.set_mode((self.settings.screen_weight, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        '''Запуск игры'''
        while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            # Установить цвет фона из настроек
            self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    AlInv = AlienInvasion()
    AlInv.run_game()
    