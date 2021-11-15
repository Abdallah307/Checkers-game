import pygame

WIDTH, HEIGHT = 800, 800

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH//COLS


#RGB COLORS

RED = (255, 0, 0)

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

BLUE = (0, 0, 255)
GREEN1 = (26,255,26)
YELLOW = (255, 255, 0)
Gray = (127,127,127)

#image crown

CROWN = pygame.transform.scale(pygame.image.load('assets/king_image.png'),(20, 14)) 