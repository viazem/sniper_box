import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    sb_settings = Settings()
    screen = pygame.display.set_mode((sb_settings.screen_width, sb_settings.screen_heigth))
    pygame.display.set_caption("Sniper box")

    # Создаем корабль
    ship = Ship(sb_settings, screen)

    # Запуск основного цикла игры
    while True:
        # Отслеживания событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update()
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(sb_settings, screen, ship)


run_game()
