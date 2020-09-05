import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, sb_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиши."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(sb_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def fire_bullet(sb_settings, screen, ship, bullets):
    # Создание новой пули и включение её в группу bullets
    if len(bullets) < sb_settings.bullets_allowed:
        new_bullets = Bullet(sb_settings, screen, ship)
        bullets.add(new_bullets)


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиши."""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(sb_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sb_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(sb_settings, screen, ship, box, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(sb_settings.bg_color)
    # Все пули выводятся позади изображения корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    box.blitme()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(sb_settings, bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиции пуль
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.right >= sb_settings.screen_width:
            bullets.remove(bullet)
        # print(len(bullets))
