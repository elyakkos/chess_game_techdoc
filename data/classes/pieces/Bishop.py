import pygame

from data.classes.Piece import Piece

class Bishop(Piece):
    """
    Класс, представляющий шахматного слона.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение слона.
        notation (str): Обозначение фигуры ('B' для слона).
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует слона.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения фигуры
        img_path = 'data/imgs/' + color[0] + '_bishop.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, 
            (board.tile_width - 20, board.tile_height - 20)
        )

        self.notation = 'B'  # Обозначение фигуры для шахматной записи

    def get_possible_moves(self, board):
        """
        Получает все возможные ходы для слона без учета других фигур.

        Слон перемещается по диагоналям.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список списков клеток, в которые может пойти слон.
                  Каждая диагональ представлена отдельным списком.
        """
        output = []

        # Возможные ходы по северо-восточной диагонали
        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)

        # Возможные ходы по юго-восточной диагонали
        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)

        # Возможные ходы по юго-западной диагонали
        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)

        # Возможные ходы по северо-западной диагонали
        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)

        return output
