import sys
import pygame


def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(sb_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(sb_settings.bg_color)
    ship.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
