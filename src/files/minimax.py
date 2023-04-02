'''Moduuli, joka sisältää minimax-algoritmin suorittavan luokan Minimax'''
from math import inf
from files.game import MainGame
order = [3, 2, 4, 1, 5, 0, 6]


class Minimax:
    """Luokka joka toteuttaa minimax algoritmin ja pelaa
    ihmispelaajaa vastaan"""

    def __init__(self):
        '''Alustaa luokan attributit'''
        self.game = MainGame()

    def minimax(self, board, depth, alpha, beta, max_player):
        '''Funktio, joka sisältää minimax-algoritmin'''
        if depth == 0:
            return self.score(board)

        if max_player:
            best_score = -inf
            for col in order:
                row = self.game.get_empty_row(board, col)
                if row == -1:
                    continue
                board[row][col] = 2
                score = self.minimax(board, depth-1, alpha, beta, False)
                board[row][col] = 0
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_score

        if not max_player:
            best_score = inf
            for col in order:
                row = self.game.get_empty_row(board, col)
                if row == -1:
                    continue
                board[row][col] = 1
                score = self.minimax(board, depth-1, alpha, beta, True)
                board[row][col] = 0
                best_score = min(best_score, score)
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_score

    def score(self, board):
        '''Laskee pelilaudan tilanteelle arvon'''
        value = 0

        '''Tarkistaa vaakatasoisen siirron arvon'''
        for row in range(self.game.rows):
            row_array = [int(i) for i in list(board[row, :])]
            for col in range(self.game.cols-3):
                possible_move = row_array[col:col+4]
                value += self.rate_move(possible_move)

        '''Tarkistaa pystysuuntaisen siirron arvon'''
        for col in range(self.game.cols):
            col_array = [int(i) for i in list(board[:, col])]
            for row in range(self.game.rows-3):
                possible_move = col_array[row:row+4]
                value += self.rate_move(possible_move)

        '''Tarkistaa ylöspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                possible_move = [board[row+i][col+1] for i in range(4)]
                value += self.rate_move(possible_move)

        '''Tarkistaa alaspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                possible_move = [board[row+3+i][col+1] for i in range(4)]
                value += self.rate_move(possible_move)

        return value

    def rate_move(self, possible_move):
        '''Laskee arvon mahdolliselle siirrolle'''
        score = 0
        if possible_move.count(2) == 4:
            score += 10
        elif possible_move.count(2) == 3 and possible_move.count(0) == 1:
            score += 10
        elif possible_move.count(2) == 2 and possible_move.count(0) == 1:
            score += 4
        if possible_move.count(1) == 3 and possible_move.count(0) == 1:
            score -=10
        if possible_move.count(1) == 2 and possible_move.count(0) == 2:
            score -=4

        return score


    def valid_location(self, board):
        '''Palauttaa listan vapaana olevista siirroista'''
        valid_locations = []
        for col in range(self.game.cols):
            if not self.game.is_column_full(board, col):
                valid_locations.append(col)
        return valid_locations
