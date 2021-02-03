import pygame 
from .constants import WHITE, BROWN, RED, BLUE, SQUARE_SIZE, GREY


class Piece:
    PADDING = 10
    BORDER = 2   

    def __init(self, row, col, colour):
        self.row = row 
        self.col = col 
        self.colour = colour 
        self.king = False 

        if self.colour == BROWN:
            self.direction = 1 
        else: 
            self.direction = -1 
        
        self.x = 0 
        self.y = 0 

    def calc_pose(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True 
    
    def draw(self, win): 
        radius = SQUARE_SIZE//2  -  self.PADDING 
        pygame.draw.circle(win, self.colour, (self.x, self.y),radius)
        pygame.draw.circle(win, GREY, (self.x, self,y), radius + self.BORDER)

    def __repr__(self):
        return str(self.colour)
    
