''''Moduuli, joka sisältää pelilogiikasta vastaavan luokan MainGame'''
import numpy as np

class MainGame():
    '''Luokka joka vastaa pelilogiikasta'''
    def __init__(self):


        self.rows = 6
        self.cols = 7
        self.board = self.create_board(self.rows, self.cols)
        self.top_order = [3, 2, 4, 1, 5, 0, 6]

    def create_board(self, rows, cols):
        '''Funktio, joka alustaa pelilaudan nollia sisältävänä taulukkona
        Args:
            rows: rivien määrä
            cols: sarakkeiden määrä'''
        board = [[0 for x in range(cols)] for y in range(rows)]
        return board

    def is_board_full(self, board):
        '''Tarkistaa onko pelilauta täynnä ja palauttaa tiedon boolaen arvona
        Pelilaudan ollessa täynnä pelin tulos on tasapeli'''
        full = True
        for column in range(0, 7):
            if not self.is_column_full(board, column):
                full = False

        return full

    def is_column_full(self, board, column):
        '''Funktio tarkistaa onko annettu sarake täynnä'''
        if board[5][column] != 0:
            return True
        return False

    def check_if_four(self, line):
        '''Funktio tarkastaa kumpi pelaaja on voittanut
        Palauttaa tiedon lukuarvona 1 tai 2 ja -1, jos ei kumpikaan.'''
        if line.count(1) == 4:
            return 1
        if line.count(2) == 4:
            return 2
        return -1

    def check_horizontal_win(self, board):
        '''Tarkistaa neljän suoran vaakasuunnasta'''
        for col  in range(5, -1, -1):
            row = board[col][:]
            for row_x in range(6, 2, -1):
                horizontal = [row[row_x-3], row[row_x-2], row[row_x-1], row[row_x]]
                if self.check_if_four(horizontal) == 2:
                    return 2
                if self.check_if_four(horizontal) == 1:
                    return 1
        return 0

    def check_vertical_win(self, board):
        '''Tarkistaa neljän suoran pystysuunnasta'''
        n_board = np.array(board)
        for piece in self.top_order:
            column = n_board[:, piece]
            for col in range(5, 2, -1):
                vertical = [column[col-3], column[col-2], column[col-1], column[col]]
                if self.check_if_four(vertical) == 2:
                    return 2
                if self.check_if_four(vertical) == 1:
                    return 1

        return 0

    def check_diagonal_up(self, board):
        '''Tarkistaa neljän suoran yläviistoon'''
        for col in range(5, 2, -1):
            for row in range(3, -1, -1):
                up_diagonal = [board[col][row], board[col-1][row+1],
                               board[col-2][row+2], board[col-3][row+3]]

                if self.check_if_four(up_diagonal) == 2:
                    return 2
                if self.check_if_four(up_diagonal) == 1:
                    return 1
        return 0

    def check_diagonal_down(self, board):
        '''Tarkastaa neljän suoran alaviistoon'''
        for col in range(5, 2, -1):
            for row in range(3, 7):
                down_diagonal = [board[col-3][row-3], board[col-2][row-2],
                                 board[col-1][row-1], board[col][row]]

                if self.check_if_four(down_diagonal) == 2:
                    return 2
                if self.check_if_four(down_diagonal) == 1:
                    return 1
        return 0

    def check_win(self, board):
        '''Funktio tarkastaa kumpi pelaajista voitti,
        ja palauttaa lukuarvon 1 tai 2 voittajan mukaan.
        Palauttaa 0, jos ei voittoaS'''
        horizontal = self.check_horizontal_win(board)
        vertical = self.check_vertical_win(board)
        down_diagonal = self.check_diagonal_down(board)
        up_diagonal = self.check_diagonal_up(board)
        if horizontal == 1 or vertical == 1 or down_diagonal == 1 or up_diagonal == 1:
            return 1
        if horizontal == 2 or vertical == 2 or down_diagonal == 2 or up_diagonal ==2:
            return 2
        return 0

    def get_empty_row(self, board, column):
        '''Tarkastaa alimman rivin annetusta sarakkeesta'''
        for row in range(self.rows):
            if board[row][column] == 0:
                return row

        return -1
