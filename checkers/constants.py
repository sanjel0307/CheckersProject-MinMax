import pygame 
 

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS 

#colour values 

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)

CROWN = pygame.transform.scale(pygame.image.load('checkers\Assets\crown.png'), (45, 25))

