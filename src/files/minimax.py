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
        for col in range(5, -1, -1):
            row = board[col][:]
            for x_row in range(6, 2, -1):
                hor = [row[x_row-3], row[x_row-2], row[x_row-1], row[x_row]]
                if self.count_four(hor) != 0:
                    return self.count_four(hor)
                value += self.count_three(hor)

        '''Tarkistaa pystysuuntaisen siirron arvon'''
        for row in order:
            col = n_board[:, row]
            for y_col in range(5, 2, -1):
                vert = [col[y_col-3], col[y_col-2], col[y_col-1], col[y_col]]
                if self.count_four(vert) != 0:
                    return self.count_four(vert)
                value += self.count_three(vert)

        '''Tarkistaa ylöspäin viistoon olevan siirron arvon'''
        for col in range(5,2,-1):
            for row in range(3,-1,-1):
                up_diagonal = [board[col][row],board[col-1][row+1],
                            board[col-2][row+2],board[col-3][row+3]]
                if self.count_four(up_diagonal) != 0:
                    return self.count_four(up_diagonal)
                value += self.count_three(up_diagonal)

        '''Tarkistaa alaspäin viistoon olevan siirron arvon'''
        for col in range(5,2,-1):
            for row in range(3,7):
                d_diagonal = [board[col-3][row-3], board[col-2][row-2],
                        board[col-1][row-1], board[col][row]]
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
            return 10
        return 0

    def count_four(self, line):
        '''Tarkastaa onko annetulla suoralla 4 samaa
        ja palauttaa arvon sen mukaan'''
        if line.count(1) == 4:
            return -1000
        if line.count(2) == 4:
            return 1000
        return 0
