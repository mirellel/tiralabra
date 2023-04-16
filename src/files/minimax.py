'''Moduuli, joka sisältää minimax-algoritmin suorittavan luokan Minimax'''
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

    def minimax(self, board, depth, max_player, alpha=-inf, beta=inf):
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
                score = self.minimax(board, depth-1, False, alpha, beta)
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
                score = self.minimax(board, depth-1, True, alpha, beta)
                board[row][col] = 0
                best_score = min(best_score, score)
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_score

    def best_move(self, board, depth):
        '''Kutsuu Minimax-algoritmia ja palauttaa parhaan
        mahdollisen siirron tuple-muodossa'''
        action = (-1, -1)
        top_score = -inf
        for col in order:
            row = self.game.get_empty_row(board, col)
            if row ==-1:
                continue
            board[row][col] = 2
            score = self.minimax(board, depth, False)
            board[row][col] = 0
            if score > top_score:
                top_score = score
                action = (row, col)
        return action

    def score(self, board):
        '''Laskee pelilaudan tilanteelle arvon'''
        value = 0
        n_board = np.array(board)

        '''Tarkistaa vaakatasoisen siirron arvon'''
        for row in range(self.game.rows):
            r_array = [int(i) for i in list(n_board[row, :])]
            for col in range(self.game.cols -3):
                hor = r_array[col:col+4]
                if self.count_four(hor) != 0:
                    return self.count_four(hor)
                value += self.count_three(hor)

        '''Tarkistaa pystysuuntaisen siirron arvon'''
        for col in range(self.game.cols):
            c_array = [int(i) for i in list(n_board[:, col])]
            for row in range(self.game.rows-3):
                vert = c_array[row:row+4]
                if self.count_four(vert) != 0:
                    return self.count_four(vert)
                value += self.count_three(vert)

        '''Tarkistaa ylöspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                up_diagonal = [n_board[row+i][col+i] for i in range(4)]
                if self.count_four(up_diagonal) != 0:
                    return self.count_four(up_diagonal)
                value += self.count_three(up_diagonal)

        '''Tarkistaa alaspäin viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                d_diagonal = [board[row+3-i][col+i] for i in range(4)]
                if self.count_four(d_diagonal) != 0:
                    return self.count_four(d_diagonal)
                value += self.count_three(d_diagonal)

        return value

    def count_three(self, line):
        '''Tarkastaa onko annetulla suoralla 3 samaa
        ja palauttaa arvon sen mukaan'''
        if line.count(1) == 3:
            return -100
        if line.count(2) == 3:
            return 100
        return 0

    def count_four(self, line):
        '''Tarkastaa onko annetulla suoralla 4 samaa
        ja palauttaa arvon sen mukaan'''
        if line.count(1) == 4:
            return -1000
        if line.count(2) == 4:
            return 1000
        return 0
