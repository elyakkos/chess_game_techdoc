import pygame

from data.classes.Piece import Piece

class King(Piece):
    """
    Класс, представляющий шахматного короля.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение короля.
        notation (str): Обозначение фигуры ('K' для короля).
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует короля.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения короля
        img_path = 'data/imgs/' + color[0] + '_king.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, 
            (board.tile_width - 20, board.tile_height - 20)
        )

        self.notation = 'K'  # Обозначение фигуры для шахматной записи

    def get_possible_moves(self, board):
        """
        Получает все возможные ходы короля без учета угроз от других фигур.

        Король может перемещаться на одну клетку в любом направлении.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, на которые король может пойти.
        """
        output = []
        moves = [
            (0, -1),   # север
            (1, -1),   # северо-восток
            (1, 0),    # восток
            (1, 1),    # юго-восток
            (0, 1),    # юг
            (-1, 1),   # юго-запад
            (-1, 0),   # запад
            (-1, -1),  # северо-запад
        ]

        for move in moves:
            new_pos = (self.x + move[0], self.y + move[1])
            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8:
                output.append([
                    board.get_square_from_pos(new_pos)
                ])

        return output

    def can_castle(self, board):
        """
        Проверяет, может ли король сделать рокировку.

        Рокировка возможна, если король и ладья не двигались, 
        и между ними нет фигур или угроз.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            str: Тип рокировки ('queenside', 'kingside') или None.
        """
        if not self.has_moved:
            if self.color == 'white':
                # Проверка рокировки на белой стороне
                queenside_rook = board.get_piece_from_pos((0, 7))
                kingside_rook = board.get_piece_from_pos((7, 7))
                if queenside_rook and not queenside_rook.has_moved:
                    if [board.get_piece_from_pos((i, 7)) for i in range(1, 4)] == [None, None, None]:
                        return 'queenside'
                if kingside_rook and not kingside_rook.has_moved:
                    if [board.get_piece_from_pos((i, 7)) for i in range(5, 7)] == [None, None]:
                        return 'kingside'

            elif self.color == 'black':
                # Проверка рокировки на черной стороне
                queenside_rook = board.get_piece_from_pos((0, 0))
                kingside_rook = board.get_piece_from_pos((7, 0))
                if queenside_rook and not queenside_rook.has_moved:
                    if [board.get_piece_from_pos((i, 0)) for i in range(1, 4)] == [None, None, None]:
                        return 'queenside'
                if kingside_rook and not kingside_rook.has_moved:
                    if [board.get_piece_from_pos((i, 0)) for i in range(5, 7)] == [None, None]:
                        return 'kingside'

    def get_valid_moves(self, board):
        """
        Получает все допустимые ходы короля с учетом правил шахмат.

        Учитывает угрозы от других фигур и возможность рокировки.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, на которые король может легально пойти.
        """
        output = []
        for square in self.get_moves(board):
            if not board.is_in_check(self.color, board_change=[self.pos, square.pos]):
                output.append(square)

        # Добавление рокировки в список допустимых ходов
        if self.can_castle(board) == 'queenside':
            output.append(
                board.get_square_from_pos((self.x - 2, self.y))
            )
        if self.can_castle(board) == 'kingside':
            output.append(
                board.get_square_from_pos((self.x + 2, self.y))
            )

        return output
