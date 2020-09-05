import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями выпущенными кораблем."""

    def __init__(self, sb_settings, screen, ship):
        """Создает объект пули выпущенной с корабля"""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0,0, sb_settings.bullet_width, sb_settings.bullet_hight)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.left

        # Позиция пули хранится в вещественном формате
        self.x = float(self.rect.x)

        self.color = sb_settings.bullet_color
        self.speed_factor = sb_settings.bullet_speed_factor

    def update(self):
        """Перемещаем пулю вправо по экрану."""
        # Обновление позиции пули в вещественном формате.
        self.x += self.speed_factor
        # Обновление позиции прямоугольника.
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
