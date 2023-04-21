'''Moduuli, joka sisältää luokan SinglePlayer'''
from files.two_player import MultiPlayer
from files.minimax import Minimax

class SinglePlayer(MultiPlayer):
    '''Perii MultiPlayer luokan ja vastaa pelistä teköälyä vastaan'''
    def __init__(self):
        super().__init__()
        self.depth = 2
        self.ai_player = True
        self.minimax = Minimax()

    def ai_move(self):
        '''Suorittaa tekoälyn siirron'''
        if not self.green_turn and not self.game_over:
            col, value = self.minimax.minimax(self.game.board, self.depth, True)
            if not self.game.is_column_full(self.game.board, col):
                row = self.get_empty_row(self.game.board, col)
                self.drop_piece(self.game.board, row, col, 2)

                self.green_turn = True

    def handle_player_move(self, column):
        '''Suorittaa pelaajan antaman siirron ja
        palauttaa siirron jälkeisen pelilaudan'''
        if not self.full_column(column):
            row = self.get_empty_row(self.game.board, column)
            if self.green_turn:
                player = 1
                self.green_turn = False
                self.drop_piece(self.game.board, row, column, player)

                self.check_victory()
                self.check_tie()
                self.ai_move()

            self.check_victory()
            self.check_tie()
        return self.game.board
