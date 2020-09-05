import pygame

class Ship():

    def __init__(self, sb_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.sb_settings = sb_settings

        # Закрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у левого края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Сохранение вещественной части координаты корабля
        self.center = float(self.rect.centery)
        # Флаг перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля."""
        # Обновляется атрибут center, не rect.
        if self.moving_up and self.rect.top > 0:
            self.center -= self.sb_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.sb_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centery = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
