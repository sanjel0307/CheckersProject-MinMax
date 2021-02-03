import pygame 
from .constants import BLACK, ROWS, WHITE, BROWN, SQUARE_SIZE

class Board:

    def __init__(self):
        self.board = [] 
        self.selected_piece = None 
        self.blue_left = self.red_left = 12 
        self.blue_kings = self.red_kings = 0 

    def draw_squares(self, win): 
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2): 
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass 

    