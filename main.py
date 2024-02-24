import sys 
import pygame
from settings import Settings
from ship import Ship
# from alien import AlienShip

class AlienInvasion():
    '''Класс всей игры'''

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_weight, self.settings.screen_height)) 
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # self.alien = AlienShip(self)

    def run_game(self):
        '''Запуск игры'''
        while(1):
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self._check_movement(event)

    def _check_movement(self, event):
        # Перемещение корабля
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
            # Установить цвет фона из настроек
            self.screen.fill(self.settings.bg_color)
            # Обновить положение корабля
            self.ship.blitme()
            # self.alien.blitme()
            

            pygame.display.flip()

if __name__ == '__main__':
    AlInv = AlienInvasion()
    AlInv.run_game()
    