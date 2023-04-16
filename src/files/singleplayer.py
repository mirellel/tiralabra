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
        row, col = self.minimax.best_move(self.board, self.depth)
        self.board[row][col] =2
        self.green_turn = True

    def handle_player_move(self, column):
        '''Suorittaa pelaajan antaman siirron ja
        palauttaa siirron jälkeisen pelilaudan'''
        if not self.full_column(column):
            row = self.get_empty_row(self.board, column)
            if self.green_turn:
                player = 1
                self.green_turn = False
                self.drop_piece(self.board, row, column, player)

                self.check_victory()
                self.check_tie()
                self.ai_move()

            self.check_victory()
            self.check_tie()
        return self.board
