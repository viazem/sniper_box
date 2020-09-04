import pygame

class Ship():

    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        # Закрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у левого края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Флаг перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля."""
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
