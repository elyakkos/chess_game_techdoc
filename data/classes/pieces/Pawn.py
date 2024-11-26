import pygame
from data.classes.Piece import Piece

class Pawn(Piece):
    """
    Класс, представляющий шахматную пешку.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение пешки.
        notation (str): Обозначение фигуры (пустое для пешки).
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует пешку.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения пешки
        img_path = 'data/imgs/' + color[0] + '_pawn.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, (board.tile_width - 35, board.tile_height - 35)
        )

        self.notation = ' '  # Пешка не имеет специального обозначения в шахматной нотации

    def get_possible_moves(self, board):
        """
        Получает возможные ходы пешки без учета блокировок и взятий.

        Пешка может двигаться на одну или две клетки вперед (если не двигалась ранее).

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, на которые пешка может двигаться.
        """
        output = []
        moves = []

        # Движение пешки вперед в зависимости от цвета
        if self.color == 'white':
            moves.append((0, -1))  # На одну клетку вперед
            if not self.has_moved:
                moves.append((0, -2))  # На две клетки вперед, если пешка не двигалась

        elif self.color == 'black':
            moves.append((0, 1))
            if not self.has_moved:
                moves.append((0, 2))

        # Проверяем, чтобы новая позиция была в пределах доски
        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if 0 <= new_pos[1] < 8:
                output.append(
                    board.get_square_from_pos(new_pos)
                )

        return output

    def get_moves(self, board):
        """
        Получает доступные ходы пешки с учетом блокировок и взятий.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, на которые пешка может двигаться или бить фигуры.
        """
        output = []

        # Проверяем движение вперед
        for square in self.get_possible_moves(board):
            if square.occupying_piece is not None:
                # Пешка не может двигаться вперед, если клетка занята
                break
            else:
                output.append(square)

        # Проверяем возможность взятия фигур противника
        if self.color == 'white':
            # Диагональные ходы для белой пешки
            if self.x + 1 < 8 and self.y - 1 >= 0:
                square = board.get_square_from_pos((self.x + 1, self.y - 1))
                if square.occupying_piece and square.occupying_piece.color != self.color:
                    output.append(square)
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                square = board.get_square_from_pos((self.x - 1, self.y - 1))
                if square.occupying_piece and square.occupying_piece.color != self.color:
                    output.append(square)

        elif self.color == 'black':
            # Диагональные ходы для черной пешки
            if self.x + 1 < 8 and self.y + 1 < 8:
                square = board.get_square_from_pos((self.x + 1, self.y + 1))
                if square.occupying_piece and square.occupying_piece.color != self.color:
                    output.append(square)
            if self.x - 1 >= 0 and self.y + 1 < 8:
                square = board.get_square_from_pos((self.x - 1, self.y + 1))
                if square.occupying_piece and square.occupying_piece.color != self.color:
                    output.append(square)

        return output

    def attacking_squares(self, board):
        """
        Определяет клетки, находящиеся под атакой пешки.

        Пешка атакует только диагонально, даже если там нет фигур.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, находящихся под атакой пешки.
        """
        moves = self.get_moves(board)
        # Возвращаем только диагональные клетки (атака)
        return [i for i in moves if i.x != self.x]
