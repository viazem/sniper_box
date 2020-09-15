class Game_stats():
    """Отслеживание статистики для игры Снайпер бокс."""

    def __init__(self, sb_settings):
        """Инициализирует статистику."""

        self.sb_settings = sb_settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.box_left = self.sb_settings.box_limit