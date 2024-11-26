import pygame
from data.classes.Board import Board

# Инициализация библиотеки Pygame
pygame.init()

# Размеры окна игры
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Создание объекта игровой доски
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
    """
    Отрисовывает текущую игровую доску и обновляет экран.

    Args:
        display (pygame.Surface): Экран, на котором выполняется отрисовка.
    """
    display.fill('white')  # Заливка фона белым цветом
    board.draw(display)  # Отрисовка доски
    pygame.display.update()  # Обновление экрана

if __name__ == '__main__':
    """
    Главный игровой цикл. Обрабатывает события, обновляет состояние игры 
    и управляет отрисовкой.
    """
    running = True  # Флаг для работы игрового цикла
    while running:
        mx, my = pygame.mouse.get_pos()  # Получение координат курсора мыши
        for event in pygame.event.get():
            # Завершение игры, если пользователь нажал на кнопку закрытия окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Обработка нажатия мыши
                if event.button == 1:  # Левая кнопка мыши
                    board.handle_click(mx, my)

        # Проверка состояния "шах и мат" для чёрных
        if board.is_in_checkmate('black'):
            print('Белые победили!')
            running = False
        # Проверка состояния "шах и мат" для белых
        elif board.is_in_checkmate('white'):
            print('Чёрные победили!')
            running = False

        # Отрисовка игрового экрана
        draw(screen)
