import pygame
from data.classes.Piece import Piece

class Knight(Piece):
    """
    Класс, представляющий шахматного коня.

    Наследует общие методы и атрибуты от класса Piece.

    Атрибуты:
        pos (tuple): Координаты позиции фигуры (x, y).
        color (str): Цвет фигуры ('white' или 'black').
        board (Board): Ссылка на объект шахматной доски.
        img (pygame.Surface): Изображение коня.
        notation (str): Обозначение фигуры ('N' для коня).
    """

    def __init__(self, pos, color, board):
        """
        Инициализирует коня.

        Args:
            pos (tuple): Начальная позиция фигуры (x, y).
            color (str): Цвет фигуры ('white' или 'black').
            board (Board): Ссылка на объект шахматной доски.
        """
        super().__init__(pos, color, board)

        # Загрузка и масштабирование изображения коня
        img_path = 'data/imgs/' + color[0] + '_knight.png'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, 
            (board.tile_width - 20, board.tile_height - 20)
        )

        self.notation = 'N'  # Обозначение фигуры для шахматной записи

    def get_possible_moves(self, board):
        """
        Получает все возможные ходы коня.

        Конь ходит буквой "Г": две клетки по одной оси и одна по другой.

        Args:
            board (Board): Текущая шахматная доска.

        Returns:
            list: Список клеток, на которые конь может пойти.
        """
        output = []
        # Возможные смещения для ходов коня
        moves = [
            (1, -2),  # вверх-вправо
            (2, -1),  # вправо-вверх
            (2, 1),   # вправо-вниз
            (1, 2),   # вниз-вправо
            (-1, 2),  # вниз-влево
            (-2, 1),  # влево-вниз
            (-2, -1), # влево-вверх
            (-1, -2)  # вверх-влево
        ]

        for move in moves:
            # Вычисляем новую позицию
            new_pos = (self.x + move[0], self.y + move[1])
            if (
                0 <= new_pos[0] < 8 and  # Проверяем, что x в пределах доски
                0 <= new_pos[1] < 8     # Проверяем, что y в пределах доски
            ):
                # Добавляем соответствующую клетку в список возможных ходов
                output.append([
                    board.get_square_from_pos(new_pos)
                ])

        return output
