'''Moduuli, joka sisältää minimax-algoritmin suorittavan luokan Minimax'''
import random
from math import inf
import numpy as np
from files.game import MainGame
order = [3, 2, 4, 1, 5, 0, 6]

class Minimax:
    """Luokka joka toteuttaa minimax algoritmin ja pelaa
    ihmispelaajaa vastaan"""

    def __init__(self):
        '''Alustaa luokan attributit'''
        self.game = MainGame()
        self.max_score = 1000000000000
        self.min_score = -100000000000

    def minimax(self, board, depth, max_player, alpha=-inf, beta=inf):
        '''Funktio, joka sisältää minimax-algoritmin'''

        winner = self.check_win(board)
        if winner == 2:
            return (None, self.max_score)
        if winner == 1:
            return (None, self.min_score)

        if depth == 0:
            return (None, self.score(board, 2))

        if self.game.is_board_full(self.game.board):
            return (None, 0)

        if max_player:
            max_value = -inf
            column = random.choice([i for i in range(self.game.cols)
                                    if not self.game.is_column_full(board, i)])
            for col in order:
                row = self.game.get_empty_row(board, col)
                if row == -1:
                    continue
                board[row][col] = 2
                new_score = self.minimax(board, depth-1, False, alpha, beta)[1]
                board[row][col] = 0
                if new_score > max_value:
                    max_value = new_score
                    column = col
                alpha = max(alpha, max_value)
                if alpha >= beta:
                    break
            return (column, max_value)

        else:
            min_value = inf
            column = random.choice([i for i in range(self.game.cols)
                                    if not self.game.is_column_full(board, i)])
            for col in order:
                row = self.game.get_empty_row(board, col)
                if row == -1:
                    continue
                board[row][col] = 1
                new_score = self.minimax(board, depth-1, True, alpha, beta)[1]
                board[row][col] = 0
                if new_score < min_value:
                    min_value = new_score
                    column = col
                beta = min(beta, min_value)
                if alpha >= beta:
                    break
            return (column, min_value)

    def check_win(self, board):
        '''Funktio, joka tarkastaa voiton'''
        return self.game.check_win(board)

    def score(self, board, piece):
        '''Laskee pelilaudan tilanteelle arvon'''
        value = 0
        n_board = np.array(board)
        center = [int(i) for i in list(n_board[:, 3])]
        count = center.count(piece)
        value += count*3

        '''Tarkistaa vaakatasoisen siirron arvon'''
        for row in range(self.game.rows):
            r_array = [int(i) for i in list(n_board[row, :])]
            for col in range(self.game.cols -3):
                move = r_array[col:col+4]
                value += self.rate_possible_move(move, piece)

        '''Tarkistaa pystysuuntaisen siirron arvon'''
        for col in range(self.game.cols):
            c_array = [int(i) for i in list(n_board[:, col])]
            for row in range(self.game.rows-3):
                move = c_array[row:row+4]
                value += self.rate_possible_move(move, piece)

        '''Tarkistaa ylöspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                move = [n_board[row+i][col+i] for i in range(4)]
                value += self.rate_possible_move(move, piece)

        '''Tarkistaa alaspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                move = [board[row+3-i][col+i] for i in range(4)]
                value += self.rate_possible_move(move, piece)

        return value

    def rate_possible_move(self, possible_move, piece):
        '''Funktio, joka laskee mahdolliselle siirrolle
        heuristisen arvon'''
        score = 0
        self.opponent = 1
        if possible_move.count(piece) == 4:
            score += 10
        elif possible_move.count(piece) == 3 and possible_move.count(0) == 1:
            score += 10
        elif possible_move.count(piece) == 2 and possible_move.count(0) ==2:
            score += 4
        if possible_move.count(self.opponent) == 3 and possible_move.count(0) == 1:
            score -= 10
        if possible_move.count(self.opponent) == 2 and possible_move.count(0) == 2:
            score -= 4
        return score
