import sys
import pygame

from bullet import Bullet
from box import Box

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


def update_screen(sb_settings, screen, ship, boxes, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(sb_settings.bg_color)
    # Все пули выводятся позади изображения корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    boxes.draw(screen)

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(sb_settings, screen, ship, boxes, bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиции пуль
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.right >= sb_settings.screen_width:
            bullets.remove(bullet)
        # print(len(bullets))

    # Проверка попаданий в пришельцев.
    # При обнаружении попаданийя удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, boxes, True, True)

    if len(boxes) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        bullets.empty()
        create_fleet(sb_settings, screen, boxes)


def create_box(sb_settings, screen, boxes):
    """Создает коробочку"""
    box = Box(sb_settings, screen)
    boxes.add(box)


def create_fleet(sb_settings, screen, boxes):
    """"Создаем группу коробочек"""
    create_box(sb_settings, screen, boxes)


def check_fleet_edges(sb_settings, boxes):
    """Реагирует достижение коробочки края экрана."""
    for box in boxes.sprites():
        if box.check_edges():
            change_fleet_direction(sb_settings, boxes)
            break


def change_fleet_direction(sb_settings, boxes):
    """Меняет направление движения"""
    sb_settings.fleet_direction *= -1


def update_boxes(sb_settings, boxes):
    """
    Проверяет, достигла коробочка края экрана.
    Обновляет позиции всех коробочек.
    """
    check_fleet_edges(sb_settings, boxes)
    boxes.update()