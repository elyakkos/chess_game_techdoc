import pygame

class Piece:
    """
    Базовый класс для шахматной фигуры.

    Атрибуты:
        pos (tuple): Позиция фигуры на доске (x, y).
        x (int): X-координата фигуры.
        y (int): Y-координата фигуры.
        color (str): Цвет фигуры ('white' или 'black').
        has_moved (bool): Флаг, указывающий, делала ли фигура ход.
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует шахматную фигуру.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект доски, на которой находится фигура.
        """
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.has_moved = False

    def move(self, board, square, force=False):
        """
        Перемещает фигуру на указанную клетку.

        Args:
            board (Board): Объект доски.
            square (Square): Клетка, на которую нужно переместить фигуру.
            force (bool): Принудительное выполнение хода (игнорирует проверку).

        Returns:
            bool: True, если ход выполнен, иначе False.
        """
        # Снимаем подсветку со всех клеток доски
        for i in board.squares:
            i.highlight = False

        # Проверяем допустимость хода или принудительное выполнение
        if square in self.get_valid_moves(board) or force:
            # Перемещение фигуры
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y

            prev_square.occupying_piece = None
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True

            # Превращение пешки
            if self.notation == ' ':
                if self.y == 0 or self.y == 7:
                    from data.classes.pieces.Queen import Queen
                    square.occupying_piece = Queen(
                        (self.x, self.y),
                        self.color,
                        board
                    )

            # Рокировка короля
            if self.notation == 'K':
                if prev_square.x - self.x == 2:
                    rook = board.get_piece_from_pos((0, self.y))
                    rook.move(board, board.get_square_from_pos((3, self.y)), force=True)
                elif prev_square.x - self.x == -2:
                    rook = board.get_piece_from_pos((7, self.y))
                    rook.move(board, board.get_square_from_pos((5, self.y)), force=True)

            return True
        else:
            board.selected_piece = None
            return False

    def get_moves(self, board):
        """
        Получает список возможных ходов фигуры с учетом препятствий.

        Args:
            board (Board): Объект доски.

        Returns:
            list: Список клеток, на которые фигура может двигаться.
        """
        output = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.occupying_piece is not None:
                    # Прерываем направление при встрече фигуры того же цвета
                    if square.occupying_piece.color == self.color:
                        break
                    else:
                        output.append(square)
                        break
                else:
                    output.append(square)
        return output

    def get_valid_moves(self, board):
        """
        Получает список допустимых ходов фигуры с учетом шаха.

        Args:
            board (Board): Объект доски.

        Returns:
            list: Список клеток, на которые фигура может двигаться без шаха.
        """
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)
        return output

    def attacking_squares(self, board):
        """
        Возвращает клетки, которые фигура атакует.

        Args:
            board (Board): Объект доски.

        Returns:
            list: Список атакуемых клеток.
        """
        return self.get_moves(board)
