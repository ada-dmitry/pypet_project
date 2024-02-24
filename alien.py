import pygame

class AlienShip():
    '''Модель и взаимодействие НЛО'''
    
    def __init__(self, ai_game):
        """Инициализирует НЛО и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)