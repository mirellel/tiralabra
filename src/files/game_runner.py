'''Moduuli, joka sisältää luokan Game'''
from files.game_logic import GameLogic
from files.minimax import Minimax

class Game:
    '''Luokka, joka vastaa pelin tapahtumien kulusta'''
    def __init__(self):
        '''Alustaa luokan attribuutit'''
        self.game_logic = GameLogic()
        self.minimax = Minimax()

        self.board = [[0 for x in range(7)] for y in range(6)]

        self.running = False
        self.game_over = False
        self.game_tie = False
        self.green_win = False
        self.red_win = False
        self.green_turn = True
        self.opponent = "player"
        self.depth = 0

        self.ai_player = False
        self.turns = 0

    def drop_piece(self, row, column, player):
        '''Päivittää pelilautaan annetun pelaajan siirron'''
        self.board[row][column] = player
        self.game_logic.board[row][column] = player
        self.turns += 1

    def full_column(self, column):
        '''Tarkastaa onko annettu sarake täynnä'''
        return self.game_logic.is_column_full(self.board, column)

    def check_victory(self):
        '''Tarkastaa onko pelilaudalla voittoa'''
        result = self.game_logic.check_win(self.board)
        if result == 1:
            self.green_win = True
            self.end_game()
        if result == 2:
            self.red_win = True
            self.end_game()
        return result

    def check_tie(self):
        '''Tarkastaa onko pelilaudalla tasapeliä'''
        if self.turns == 42:
            self.tie()
        else:
            return self.game_tie

    def tie(self):
        '''Lopettaa pelin tasapelin sattuessa'''
        self.game_tie = True
        self.end_game()

    def get_empty_row(self, column):
        '''Hakee alimman vapaan rivin annetulta sarakkeelta'''
        row = self.game_logic.get_empty_row(self.board, column)
        return row

    def restart(self):
        '''Asettaa pelin attribuutit aloitustilaan
        ja tyhjentää pelilaudan'''
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.running = False

        self.game_over = False
        self.game_tie = False
        self.mouse_position = (0,0)

        self.green_win = False
        self.red_win = False
        self.green_turn = True
        self.turns = 0
        self.ai_player = False

    def end_game(self):
        '''Asettaa pelin päättyneeksi'''
        self.game_over = True

    def handle_player_move(self, column):
        '''Suorittaa pelaajan antaman siirron ja
        palauttaa siirron jälkeisen pelilaudan'''
        if not self.full_column(column) and not self.game_over:
            row = self.get_empty_row(column)
            if self.green_turn:
                player = 1
                self.green_turn = False
            else:
                player = 2
                self.green_turn = True
            self.drop_piece(row, column, player)
            self.check_tie()
            self.check_victory()
        return self.board

    def handle_ai_move(self):
        '''Suorittaa tekoälyn siirron'''
        if not self.green_turn and not self.game_over:
            col = self.minimax.minimax(self.board, self.depth, True)[0]
            if not self.full_column(col):
                row = self.get_empty_row(col)
                self.drop_piece(row, col, 2)
                self.check_victory()
                self.check_tie()
                self.green_turn = True
        return self.board
