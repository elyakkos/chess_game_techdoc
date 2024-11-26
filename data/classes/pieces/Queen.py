import pygame
from data.classes.Piece import Piece

class Queen(Piece):
    """
    Класс, представляющий шахматную ферзя.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение ферзя.
        notation (str): Обозначение ферзя в шахматной нотации ('Q').
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует ферзя.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения ферзя
        img_path = 'data/imgs/' + color[0] + '_queen.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'Q'  # Обозначение ферзя в шахматной нотации

    def get_possible_moves(self, board):
        """
        Получает все возможные ходы для ферзя с учетом его перемещений по диагоналям и прямым линиям.

        Ферзь может двигаться на любую клетку в любом из 8 направлений:
        - на север
        - на северо-восток
        - на восток
        - на юго-восток
        - на юг
        - на юго-запад
        - на запад
        - на северо-запад

        Ходы продолжаются до тех пор, пока не столкнутся с границей доски или другой фигурой.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список возможных ходов ферзя.
        """
        output = []

        # Движение на север (по вертикали)
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_north)

        # Движение на северо-восток (диагональ)
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos((self.x + i, self.y - i)))
        output.append(moves_ne)

        # Движение на восток (по горизонтали)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_east)

        # Движение на юго-восток (диагональ)
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos((self.x + i, self.y + i)))
        output.append(moves_se)

        # Движение на юг (по вертикали)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_south)

        # Движение на юго-запад (диагональ)
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos((self.x - i, self.y + i)))
        output.append(moves_sw)

        # Движение на запад (по горизонтали)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_west)

        # Движение на северо-запад (диагональ)
        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board.get_square_from_pos((self.x - i, self.y - i)))
        output.append(moves_nw)

        return output
