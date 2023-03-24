'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame

class GameUI:
    """Luokka, joka vastaa pelilaudan UI:sta"""

    def __init__(self):
        """Alustaa pelin attribuutit"""

        '''Pelilaudan rivien ja sarakkeiden määrät, pelilaudan koko'''
        self.rows = 6
        self.cols = 7
        self.square_size = 100
        self.width = self.cols*self.square_size
        self.height = (self.rows+1)*self.square_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4")

        self.radius = self.square_size//2-5

        self.blue = (111, 163, 189)
        self.white = (255, 255, 255)

    def draw_board(self):
        '''Funktio, joka piirtää pelilaudan, joka koostuu neiliöistä ja ympyröistä.'''
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, self.blue, (col*self.square_size,
                                                          row*self.square_size+self.square_size,
                                                          self.square_size, self.square_size))

        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.circle(self.screen, self.white, (col*self.square_size+
                                                            self.square_size//2,
                                                            self.height-(row*self.square_size+
                                                            self.square_size//2)),
                                                            self.radius)

        return self.screen
