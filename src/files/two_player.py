'''Tähän tulee koodi, joka vastaa kahden ihmispelaajan välisestä pelistä'''
import pygame
from UI.game_ui import GameUI
from files.game import MainGame

class MultiPlayer():

    def __init__(self):
        self.ui = GameUI()
        self.game = MainGame()
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False
        
        self.game_over = False
        self.mouse_position = (0,0)

        self.green_win = False
        self.red_win = False
        self.green_turn = True
        self.red_turn = False

    def run(self):
        while True:
            pygame.init()
            self.running = True
            self.ui.setup()
            self.gameloop()
            break

    def gameloop(self):
        while self.running:
            self.check_events()
            self.ui.draw_board(self.board, self.game_over, self.mouse_position, self.green_turn, self.green_win, self.red_win)


    def check_events(self):
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
        if not self.full_column(column):
            row = self.get_empty_row(self.board, column)
            if self.green_turn:
                player = 1
                self.green_turn = False
            else:
                player = 2
                self.green_turn = True
            self.drop_piece(self.board, row, column, player)
            self.check_victory()

    def drop_piece(self, board, row, column, player):
        board[row][column] = player 
    
    def full_column(self, column):
        return self.game.is_column_full(self.board, column)
    

    def check_victory(self):
        result = self.game.check_win(self.board)
        if result == 1:
            self.green_win = True
            self.game_over = True
        if result == 2:
            self.red_win = True
            self.game_over = True

    def check_tie(self):
        if self.game.is_board_full(self.board):
            self.tie()

    def tie(self):
        self.game_over = True

    def get_empty_row(self, board, column):
        for row in range(0, 6):
            if board[row][column] == 0:
                return row
            
    def restart(self):
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False
        
        self.game_over = False
        self.mouse_position = (0,0)

        self.green_win = False
        self.red_win = False
        self.green_turn = True
        self.red_turn = False
