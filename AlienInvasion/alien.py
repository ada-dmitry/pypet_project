# import pygame

# # print('Привет, Дима!')
# class AlienShip():
#     '''Модель и взаимодействие НЛО'''
    
#     def __init__(self, ai_game):
#         """Инициализирует НЛО и задает его начальную позицию."""
#         self.screen = ai_game.screen
#         self.screen_rect = ai_game.screen.get_rect()
#         # Загружает изображение корабля и получает прямоугольник.
#         self.image = pygame.image.load('image/alien.bmp')
#         self.rect = self.image.get_rect()
#         # Каждый новый корабль появляется у нижнего края экрана.
#         self.rect.center = self.screen_rect.center

#         def update(self):
#         '''Обновление позиции корабля игрока'''
#         while(1):
#             if self.rect.right < self.screen_rect.right:
#                 self.x += self.settings.ship_speed
#             if self.rect.left > 0:
#                 self.x -= self.settings.ship_speed
#             self.rect.x = self.x

#     def blitme(self):
#         """Рисует корабль в текущей позиции."""
#         self.screen.blit(self.image, self.rect)