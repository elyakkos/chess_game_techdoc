import pygame
from data.classes.Board import Board

class Game:
    """
    Класс Game управляет основным игровым процессом, включая главное меню и игровой цикл.

    Attributes:
        WINDOW_SIZE (tuple): Размеры окна игры (ширина, высота).
        screen (pygame.Surface): Поверхность для отрисовки.
        WHITE (tuple): Цвет для белого.
        BLACK (tuple): Цвет для чёрного.
        GRAY (tuple): Цвет для серого.
        font (pygame.font.Font): Шрифт для отображения текста.
        board (Board): Объект класса Board для управления шахматной доской.
    """

    def __init__(self):
        """
        Инициализирует объект Game, задавая параметры окна, цвета, шрифт и шахматную доску.
        """
        pygame.init()
        self.WINDOW_SIZE = (600, 600)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Chess Game")

        # Цвета
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)

        # Шрифт
        self.font = pygame.font.Font(None, 36)

        # Доска
        self.board = Board(self.WINDOW_SIZE[0], self.WINDOW_SIZE[1])

    def draw_text(self, surface, text, color, x, y):
        """
        Отображает текст на указанной поверхности.

        Args:
            surface (pygame.Surface): Поверхность, на которой будет отображаться текст.
            text (str): Текст для отображения.
            color (tuple): Цвет текста (RGB).
            x (int): Координата X текста.
            y (int): Координата Y текста.
        """
        text_surface = self.font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def main_menu(self):
        """
        Отображает главное меню игры с кнопками "Начать игру" и "Выход".
        """
        menu_running = True
        while menu_running:
            self.screen.fill(self.WHITE)
            self.draw_text(self.screen, "Chess Game", self.BLACK, self.WINDOW_SIZE[0] // 2 - 80, 100)

            # Кнопки меню
            play_button = pygame.Rect(self.WINDOW_SIZE[0] // 2 - 100, 200, 200, 50)
            quit_button = pygame.Rect(self.WINDOW_SIZE[0] // 2 - 100, 300, 200, 50)

            pygame.draw.rect(self.screen, self.GRAY, play_button)
            pygame.draw.rect(self.screen, self.GRAY, quit_button)

            self.draw_text(self.screen, "Начать игру", self.BLACK, self.WINDOW_SIZE[0] // 2 - 70, 210)
            self.draw_text(self.screen, "Выход", self.BLACK, self.WINDOW_SIZE[0] // 2 - 40, 310)

            pygame.display.update()

            # Обработка событий
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

    def game_loop(self):
        """
        Основной игровой цикл, который управляет процессом игры, обработкой событий и отрисовкой.
        """
        running = True
        while running:
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.board.handle_click(mx, my)

            # Проверка состояния игры
            if self.board.is_in_checkmate('black'):
                pygame.display.set_caption("Chess Game - Белые победили!")
                print("Белые победили!")
                running = False
            elif self.board.is_in_checkmate('white'):
                pygame.display.set_caption("Chess Game - Черные победили!")
                print("Черные победили!")
                running = False
            else:
                current_turn = "Ход: Белые" if self.board.turn == "white" else "Ход: Черные"
                pygame.display.set_caption(f"Chess Game - {current_turn}")

            # Отрисовка доски и интерфейса
            self.screen.fill(self.WHITE)
            self.board.draw(self.screen)
            pygame.display.update()

    def run(self):
        """
        Запускает игру, начиная с главного меню и переходя к игровому циклу.
        """
        self.main_menu()
        self.game_loop()
        pygame.quit()

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
