import pygame
from data.classes.Piece import Piece

class Rook(Piece):
    """
    Класс, представляющий шахматную ладью.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение ладьи.
        notation (str): Обозначение ладьи в шахматной нотации ('R').
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует ладью.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения ладьи
        img_path = 'data/imgs/' + color[0] + '_rook.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

        self.notation = 'R'  # Обозначение ладьи в шахматной нотации

    def get_possible_moves(self, board):
        """
        Получает все возможные ходы для ладьи.

        Ладья может двигаться на любую клетку по вертикали или горизонтали,
        пока не столкнется с другой фигурой или границей доски.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список возможных ходов ладьи.
        """
        output = []

        # Движение на север (по вертикали)
        moves_north = []
        for y in range(self.y)[::-1]:
            moves_north.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_north)

        # Движение на восток (по горизонтали)
        moves_east = []
        for x in range(self.x + 1, 8):
            moves_east.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_east)

        # Движение на юг (по вертикали)
        moves_south = []
        for y in range(self.y + 1, 8):
            moves_south.append(board.get_square_from_pos((self.x, y)))
        output.append(moves_south)

        # Движение на запад (по горизонтали)
        moves_west = []
        for x in range(self.x)[::-1]:
            moves_west.append(board.get_square_from_pos((x, self.y)))
        output.append(moves_west)

        return output
