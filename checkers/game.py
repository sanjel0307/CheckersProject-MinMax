import pygame 
from .constants import * 
from .board import Board 

class Game: 

    def __init__(self, win):
        self._init()
        self.win = win 
    

    def update(self):
        self.board.draw(self.win)
        self._draw_valid_moves(self.valid_moves)
        pygame.display.update() 

    def _init(self):
        self.selected = None 
        self.board = Board() 
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()
    
    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False



    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True


    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED
    
    def _draw_valid_moves(self, moves): 
        for move in moves:
            row, col = move 
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    
    
