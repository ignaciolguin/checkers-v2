import pygame
from .constants import BLACK, RED, WHITE, ROWS, SQUARE_SIZE


class Board:

    def __init__(self):

        self.board = [[WHITE, 0, WHITE, 0, WHITE],
                      [RED, 0, RED, 0, RED]]

        self.selected_piece = None

        # self.red_left = self.white_left
        # self.red_kings = self.white_kings

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE,
                                 col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
