class Settings():
    """Класс для хранения всех настроек игры Снайпер бокс."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (102, 178, 255)
        # Настройка корабля
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 15
        self.bullet_hight = 3
        self.bullet_color = (204, 255, 255)
        self.bullets_allowed = 3
        # Настройка коробочек
        self.box_speed_factor = 0.05
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.box_limit = 3
        # Игра Снайпер бокс запускается в активном режиме.
        self.game_active = True
