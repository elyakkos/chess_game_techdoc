import pygame

class Square:
    """
    Класс, представляющий клетку шахматной доски.

    Атрибуты:
        x (int): Координата X клетки на доске.
        y (int): Координата Y клетки на доске.
        width (int): Ширина клетки.
        height (int): Высота клетки.
        abs_x (int): Абсолютная X-координата для отрисовки.
        abs_y (int): Абсолютная Y-координата для отрисовки.
        abs_pos (tuple): Абсолютная позиция клетки (abs_x, abs_y).
        pos (tuple): Позиция клетки на доске (x, y).
        color (str): Цвет клетки ('light' или 'dark').
        draw_color (tuple): Цвет клетки для отрисовки.
        highlight_color (tuple): Цвет подсветки клетки.
        occupying_piece (Piece or None): Фигура, находящаяся на клетке (если есть).
        coord (str): Шахматная координата клетки (например, "a1").
        highlight (bool): Флаг, указывающий, подсвечивается ли клетка.
        rect (pygame.Rect): Объект прямоугольника для отрисовки.
    """

    def __init__(self, x, y, width, height):
        """
        Инициализирует клетку шахматной доски.

        Args:
            x (int): Координата X клетки на доске.
            y (int): Координата Y клетки на доске.
            width (int): Ширина клетки.
            height (int): Высота клетки.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Абсолютные координаты для отрисовки
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)

        # Шахматная позиция и цвет
        self.pos = (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 189, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None  # Фигура, находящаяся на клетке
        self.coord = self.get_coord()  # Шахматная координата клетки
        self.highlight = False  # Подсвечивается ли клетка

        # Прямоугольник для отрисовки клетки
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    def get_coord(self):
        """
        Генерирует шахматную координату клетки.

        Returns:
            str: Шахматная координата клетки (например, "a1").
        """
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        """
        Отрисовывает клетку на экране.

        Args:
            display (pygame.Surface): Поверхность для отрисовки.
        """
        # Отрисовка с учетом подсветки
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)

        # Если на клетке есть фигура, отрисовать её
        if self.occupying_piece is not None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
