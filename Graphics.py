import time, pygame

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (224, 224, 224)
black = (12, 12, 12)
pink = (255, 200, 200)


class Graphics:
    def __init__(self, start_board):
        self.width = 500
        self.height = 500
        self.rectangle_tuples = [(0, 0, self.width/3, self.height/3),
                                 (self.width/3, 0, self.width/3, self.height/3),
                                 (self.width / 3 * 2, 0, self.width/3, self.height/3),
                                 (0, self.height/3, self.width/3, self.height/3),
                                 (self.width / 3, self.height/3, self.width / 3, self.height / 3),
                                 (self.width / 3 * 2, self.height/3, self.width / 3, self.height / 3),
                                 (0, self.height / 3 * 2, self.width / 3, self.height / 3),
                                 (self.width / 3, self.height / 3 * 2, self.width / 3, self.height / 3),
                                 (self.width / 3 * 2, self.height / 3 * 2, self.width / 3, self.height / 3),
                                 ]
        pygame.init()
        pygame.display.set_caption('8Puzzle Solver')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.update(start_board)
        time.sleep(3)

    def draw_rects(self):
        for i in range(0, 9):
            pygame.draw.rect(self.screen, white, self.rectangle_tuples[i], 5)

    def draw_numbers(self, board_list, font_size):
        for i in range(0, 9):
            my_font = pygame.font.SysFont('fixedsys', font_size)
            # only print a blank square for the 0
            if board_list[i] != 0:
                text_surface = my_font.render(str(board_list[i]), False, green)
            else:
                text_surface = my_font.render("", False, green)  # 8 and 10 below are just to help center the # in grid
            self.screen.blit(text_surface, (self.rectangle_tuples[i][0] + self.width / 8,
                                            self.rectangle_tuples[i][1] + self.height / 10))

    def draw_board(self, width, height, board, order, font_size, h_padding):
        padding = width * order + (15 * order)
        height_padding = h_padding
        self.rectangle_tuples = [(0 + padding, 0 + height_padding, width / 3, height / 3),
                                 (width / 3 + padding, 0 + height_padding, width / 3, height / 3),
                                 (width / 3 * 2 + padding, 0 + height_padding, width / 3, height / 3),
                                 (0 + padding, height / 3 + height_padding, width / 3, height / 3),
                                 (width / 3 + padding, height / 3 + height_padding, width / 3, height / 3),
                                 (width / 3 * 2 + padding, height / 3 + height_padding, width / 3, height / 3),
                                 (0 + padding, height / 3 * 2 + height_padding, width / 3, height / 3),
                                 (width / 3 + padding, height / 3 * 2 + height_padding, width / 3, height / 3),
                                 (width / 3 * 2 + padding, height / 3 * 2 + height_padding, width / 3, height / 3),
                                 ]
        self.draw_rects()
        self.draw_numbers(board, font_size)

    def update(self, board_list):
        self.screen.fill(black)
        self.draw_board(self.width, self.height, board_list, 0, 150, 0)
        pygame.display.update()

    def show_solution(self, path_to_solution):
        board_width = 115 * len(path_to_solution)
        self.screen = pygame.display.set_mode((board_width, 200))
        self.width = 100
        self.height = 150
        for item, i in zip(path_to_solution, range(0, len(path_to_solution))):
            self.draw_board(self.width, self.height, item.board.board_list, i, 30, 15)
        pygame.display.update()

    def wait_to_close(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

