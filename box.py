import pygame
from pygame.sprite import Sprite
from random import randint


class Box(Sprite):
    """Клас представляющий одну коробочку."""

    def __init__(self, sb_settings, screen):
        """Инициализирует коробочку и задает её начальную позицию."""
        super().__init__()
        self.screen = screen
        self.sb_settings = sb_settings

        # Закрузка изображения коробочки и получение прямоугольника.
        self.image = pygame.image.load('images/box.png')
        self.rect = self.image.get_rect()

        # Каждая коробочка появляется в случайной позиции справа экрана.
        self.rect.x = (self.sb_settings.screen_width - self.rect.width)
        self.rect.y = (self.rect.height + randint(0, int((self.sb_settings.screen_height - self.rect.height * 2) / 2)))

        # Сохранение точной позиции пришельца.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Возвращает True если коробочка у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Перемещает коробочку вверх или вниз."""
        self.y -= (self.sb_settings.box_speed_factor * self.sb_settings.fleet_direction)
        self.rect.y = self.y

    def blitme(self):
        """Выводит коробочку в текущем положении"""
        self.screen.blit(self.image, self.rect)