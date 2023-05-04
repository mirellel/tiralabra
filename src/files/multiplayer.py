'''Moduuli, johon kuuluu pelistä vastaava luokka MultiPlayer'''
import pygame
from files.game_runner import Game
from UI.game_ui import GameUI

class MultiPlayer:
    '''Luokka, joka vastaa kahden pelaajan välisestä pelistä'''
    def __init__(self):
        '''Alustaa luokan attribuutit'''
        self.game = Game()
        self.game_ui = GameUI()
        self.mouse_position = (0,0)
        self.game.opponent = "player"

    def run(self):
        '''Alustaa pelin pyörimisen'''
        while True:
            pygame.init()
            self.game.running = True
            self.game_ui.setup()
            self.gameloop()
            break

    def gameloop(self):
        '''Päivittää ruutua ja pelitilannetta silmukassa pelin
        ollessa käynnissä'''
        while self.game.running:
            self.check_events()
            self.game_ui.draw_board(self.game.board, self.game.game_over,
                               self.mouse_position, self.game.green_turn,
                               self.game.green_win, self.game.red_win, self.game.ai_player,
                               self.game.game_tie, self.game.opponent)
    def check_events(self):
        '''Tarkastaa pygametapahtumat ja kutstuu
        tarvitavat funktiot suorittamaan loogiset siirrot'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    x_position = position[0]
                    col = x_position // 100
                    self.game.handle_player_move(col)

            if event.type == pygame.MOUSEMOTION:
                self.mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.game.restart()
                if event.key == pygame.K_e:
                    exit()
