import numpy as np
import pygame
from pygame.locals import *


class Board:
    """Luokka, joka vastaa pelilautaa"""

    def __init__(self):
        """Alustaa pelin attribuutit"""

        pygame.init()
        self.rows = 6
        self.cols = 7
        self.square_size = 100
        self.width = self.cols*self.square_size
        self.height = (self.rows+1)*self.square_size

        self.board = self.create_board(self.rows, self.cols)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4")

        self.radius = self.square_size//2-5

        self.blue = (111, 163, 189)
        self.white = (255, 255, 255)

    def create_board(self, rows, cols):
        board = np.zeros((rows, cols))
        return board
    
    def draw_board(self, board):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, self.blue, (col*self.square_size, 
                                                          row*self.square_size+self.square_size,
                                                          self.square_size, self.square_size))
                
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.circle(self.screen, self.white, (col*self.square_size+self.square_size//2,
                                                            self.height-(row*self.square_size+self.square_size//2)),
                                                            self.radius)

        return self.screen

        