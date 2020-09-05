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

    def blitme(self):
        """Выводит коробочку в текущем положении"""
        self.screen.blit(self.image, self.rect)