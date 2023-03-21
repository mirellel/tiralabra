import sys
import pygame
from board import Board

class MainGame():

    def __init__(self):

        pygame.init()
        self.game = Board()
        self.game_over = False
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.game.draw_board(self.game.board)
            pygame.display.update()


        pygame.time.wait(3000)