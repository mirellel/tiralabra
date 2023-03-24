import sys
import pygame
from UI.game_ui import GameUI


class MainGame():
    '''Luokka, joka vastaa pelin tapahtumien käsittelystä'''
    def __init__(self):

        pygame.init()
        self.game = GameUI()
        self.game_over = False

        self.rows = 6
        self.cols = 7
        self.board = self.create_board(self.rows, self.cols)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.game.draw_board()
            pygame.display.update()

        pygame.time.wait(3000)

    def create_board(self, rows, cols):
        '''Funktio, joka alustaa pelilaudan nollia sisältävänä taulukkona
        Args:
            rows: rivien määrä
            cols: sarakkeiden määrä'''
        board = [[0 for x in range(cols)] for y in range(rows)]
        return board
