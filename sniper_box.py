import sys
import pygame

from settings import Settings


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    sb_settings = Settings()
    screen = pygame.display.set_mode((sb_settings.screen_width, sb_settings.screen_heigth))
    pygame.display.set_caption("Sniper box")

    # Запуск основного цикла игры
    while True:
        # Отслеживания событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(sb_settings.bg_color)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
