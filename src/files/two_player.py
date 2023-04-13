'''Moduuli, johon kuuluu pelistä vastaava luokka MultiPlayer'''
import pygame
from UI.game_ui import GameUI
from files.game import MainGame

class MultiPlayer:
    '''Luokka, joka vastaa kahden pelaajan välisestä pelistä'''
    def __init__(self):
        '''Alustaa luokan attribuutit'''
        self.game_ui = GameUI()
        self.game = MainGame()
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False

        self.game_over = False
        self.mouse_position = (0,0)

        self.green_win = False
        self.red_win = False
        self.green_turn = True
        self.ai_player = False

    def run(self):
        '''Alustaa pelin pyörimisen'''
        while True:
            pygame.init()
            self.running = True
            self.game_ui.setup()
            self.gameloop()
            break

    def gameloop(self):
        '''Päivittää ruutua ja pelitilannetta silmukassa pelin
        ollessa käynnissä'''
        while self.running:
            self.check_events()
            self.game_ui.draw_board(self.board, self.game_over,
                               self.mouse_position, self.green_turn,
                               self.green_win, self.red_win, self.ai_player)


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
                    self.handle_player_move(col)

            if event.type == pygame.MOUSEMOTION:
                self.mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()
                if event.key == pygame.K_e:
                    exit()

    def handle_player_move(self, column):
        '''Suorittaa pelaajan antaman siirron ja
        palauttaa siirron jälkeisen pelilaudan'''
        if not self.full_column(column):
            row = self.get_empty_row(self.board, column)
            if self.green_turn:
                player = 1
                self.green_turn = False
                if self.ai_player == True:
                    self.ai_turn = True
            else:
                player = 2
                self.green_turn = True
            self.drop_piece(self.board, row, column, player)
            self.check_victory()
        return self.board

    def drop_piece(self, board, row, column, player):
        '''Päivittää pelilautaan annetun pelaajan siirron'''
        board[row][column] = player

    def full_column(self, column):
        '''Tarkastaa onko annettu sarake täynnä'''
        return self.game.is_column_full(self.board, column)


    def check_victory(self):
        '''Tarkastaa onko pelilaudalla voittoa'''
        result = self.game.check_win(self.board)
        if result == 1:
            self.green_win = True
            self.game_over = True
        if result == 2:
            self.red_win = True
            self.game_over = True
        return result

    def check_tie(self):
        '''Tarkastaa onko pelilaudalla tasapeliä'''
        if self.game.is_board_full(self.board):
            self.tie()

    def tie(self):
        '''Lopettaa pelin tasapelin sattuessa'''
        self.game_over = True

    def get_empty_row(self, board, column):
        '''Hakee alimman vapaan rivin annetulta sarakkeelta'''
        row = self.game.get_empty_row(board, column)
        return row

    def restart(self):
        '''Asettaa pelin attribuutit aloitustilaan
        ja tyhjentää pelilaudan'''
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False

        self.game_over = False
        self.mouse_position = (0,0)

        self.green_win = False
        self.red_win = False
        self.green_turn = True
