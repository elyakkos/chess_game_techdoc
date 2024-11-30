import pygame
from data.classes.Board import Board

# Инициализация Pygame
pygame.init()

# Параметры окна
WINDOW_SIZE = (600, 600)
"""tuple: Размеры окна игры (ширина, высота) в пикселях."""

screen = pygame.display.set_mode(WINDOW_SIZE)
"""pygame.Surface: Основное окно игры."""

pygame.display.set_caption("Chess Game")
"""str: Заголовок окна игры."""

# Цвета
WHITE = (255, 255, 255)
"""tuple: Белый цвет для фона (RGB)."""

BLACK = (0, 0, 0)
"""tuple: Черный цвет для текста (RGB)."""

GRAY = (200, 200, 200)
"""tuple: Серый цвет для кнопок (RGB)."""

# Шрифт
font = pygame.font.Font(None, 36)
"""pygame.Font: Шрифт для текста в игре."""

# Инициализация доски
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
"""Board: Игровая шахматная доска."""

def draw_text(surface, text, color, x, y):
    """
    Отображает текст на экране.

    Args:
        surface (pygame.Surface): Поверхность, на которой рисуется текст.
        text (str): Текст для отображения.
        color (tuple): Цвет текста в формате RGB.
        x (int): Координата X для текста.
        y (int): Координата Y для текста.
    """
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def main_menu():
    """
    Отображает главное меню игры с кнопками "Начать игру" и "Выход".

    Обработка событий:
        - Кнопка "Начать игру" начинает игру.
        - Кнопка "Выход" завершает программу.

    Меню работает в отдельном цикле, пока игрок не выберет действие.
    """
    menu_running = True
    while menu_running:
        screen.fill(WHITE)
        
        # Заголовок
        draw_text(screen, "Chess Game", BLACK, WINDOW_SIZE[0] // 2 - 80, 100)
        
        # Кнопки
        play_button = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 200, 200, 50)
        quit_button = pygame.Rect(WINDOW_SIZE[0] // 2 - 100, 300, 200, 50)
        
        pygame.draw.rect(screen, GRAY, play_button)
        pygame.draw.rect(screen, GRAY, quit_button)
        
        draw_text(screen, "Начать игру", BLACK, WINDOW_SIZE[0] // 2 - 70, 210)
        draw_text(screen, "Выход", BLACK, WINDOW_SIZE[0] // 2 - 40, 310)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    menu_running = False
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

def game_loop():
    """
    Основной игровой цикл.

    В цикле обрабатываются следующие события:
        - Движения мыши.
        - Нажатия кнопок мыши.
        - Проверка состояния игры на шах и мат.

    Также обновляется заголовок окна с указанием текущего игрока или победителя.
    """
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    board.handle_click(mx, my)

        # Проверка на мат
        if board.is_in_checkmate('black'):
            pygame.display.set_caption("Chess Game - Белые победили!")
            print("Белые победили!")
            running = False
        elif board.is_in_checkmate('white'):
            pygame.display.set_caption("Chess Game - Черные победили!")
            print("Черные победили!")
            running = False
        else:
            # Обновление заголовка окна в зависимости от текущего хода
            current_turn = "Ход: Белые" if board.turn == "white" else "Ход: Черные"
            pygame.display.set_caption(f"Chess Game - {current_turn}")

        # Отрисовка игры
        screen.fill(WHITE)
        board.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    """
    Точка входа в программу.

    Сначала отображается главное меню (`main_menu()`), затем запускается основной игровой цикл (`game_loop()`).
    """
    main_menu()  # Показываем главное меню
    game_loop()  # Запускаем игровой цикл
    pygame.quit()
