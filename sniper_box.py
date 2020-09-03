import sys
import pygame


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sniper box")

    # Запуск основного цикла игры
    while True:
        # Отслеживания событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
