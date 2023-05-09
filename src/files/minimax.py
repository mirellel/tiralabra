'''Moduuli, joka sisältää minimax-algoritmin suorittavan luokan Minimax'''
from math import inf
import numpy as np
from files.game_logic import MainGame
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
        '''Palauttaa parhaan mahdollisen siirron tietokone-pelaajalle
        käyttäen minimax algoritmia  tehostettuna alpha-beta-karsinnalla
        Muuttujat:
            board (list): Listoitsta koostuva lista, joka kuvaa pelilautaa
            depth (int): hakupuun syvyys
            max_player (bool): Totuusarvo, joka kertoo onko tietokoneen vuoro tehdä siirto
            alpha (int): Maksimi arvo löytyneiden siirtojen alarajalle
            beta (int): Minimiarvo mahdollisten siirtojen ylärajalle
        Palautusarvo:
            column (int): sarake, johon siirto tehdään
            max_value / min_value (int): Lukuarvo, joka kuvaa kuinka hyvä siirto on'''

        winner = self.check_win(board)
        valid_locations = self.get_valid_locations(board)

        if self.game.is_board_full(self.game.board):
            return (None, 0)

        if not valid_locations:
            return (None, 0)

        if depth == 0 or winner > 0:
            if winner > 0:
                if winner == 2:
                    return (None, self.max_score)
                if winner == 1:
                    return (None, self.min_score)
            else:
                return (None, self.score(board, 2))

        if max_player:
            max_value = -inf
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

        '''Tarkistaa oikealle viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3):
                move = [n_board[row+i][col+i] for i in range(4)]
                value += self.rate_possible_move(move, piece)

        '''Tarkistaa vasemmalle viistoon olevan siirron arvon'''
        for row in range(self.game.rows-3):
            for col in range(self.game.cols-3, 0, -1):
                move = [board[row+i][col-i] for i in range(4)]
                value += self.rate_possible_move(move, piece)

        return value

    def rate_possible_move(self, possible_move, piece):
        '''Funktio, joka laskee mahdolliselle siirrolle
        heuristisen arvon'''
        score = 0
        self.opponent = 1
        if piece == 1:
            self.opponent = 2
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

    def get_valid_locations(self, board):
        '''
        Palauttaa listan mahdollisista sarakkeista, joihin voidaan tehdä siirto
        '''
        valid_locations = []
        for col in range(7):
            if not self.game.is_column_full(board, col):
                valid_locations.append(col)
        return valid_locations
