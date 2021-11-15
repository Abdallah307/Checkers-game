import pygame
from .constants import CROWN, RED, WHITE,Gray,WIDTH,COLS
class Piece:

    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col , color):

        self.row = row
        self.col = col
        self.color = color
        self.king = False



        self.x = 0
        self.y =0
        self.calc_pos()


    def calc_pos(self):
        self.x = WIDTH//COLS * self.col + WIDTH//COLS // 2     # to set the piece in the center of square
        self.y = WIDTH//COLS * self.row + WIDTH//COLS // 2 

    
    def make_king(self):
        self.king = True

    def draw(self, win):

        radius = WIDTH//COLS // 2 - self.PADDING
        pygame.draw.circle(win, Gray, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2,self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()   


        