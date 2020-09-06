import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from box import Box

import game_functions as gf


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    sb_settings = Settings()
    screen = pygame.display.set_mode((sb_settings.screen_width, sb_settings.screen_height))
    pygame.display.set_caption("Sniper box")

    # Создаем корабль
    ship = Ship(sb_settings, screen)
    # Создаем группы для хранения пуль
    bullets = Group()
    boxes = Group()

    # Создаём группу для коробочек
    gf.create_fleet(sb_settings, screen, boxes)

    # Запуск основного цикла игры
    while True:
        # Отслеживания событий клавиатуры и мыши.
        gf.check_events(sb_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(sb_settings, boxes, bullets)
        gf.update_boxes(sb_settings, boxes)

        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(sb_settings, screen, ship, boxes, bullets)


run_game()
