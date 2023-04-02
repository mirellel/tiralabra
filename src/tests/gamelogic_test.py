'''Moduuli, joka sisältää testiluokan TestGame'''
import unittest
import os
from files.game import MainGame
os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestGame(unittest.TestCase):
    '''Testiluokka game_logic tiedostossa oleville funktioille'''
    def setUp(self):
        self.top_order = [3, 2, 4, 1, 5, 0, 6]
        self.game = MainGame()

    def test_create_board_returns_empty_board(self):
        '''Testaa MainGame luokan funktiota create_board()
        ja tarkastaa, että se palauttaa tyhjän laudan'''
        board = self.game.create_board(6, 7)
        empty_board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(board, empty_board)

    def test_is_board_full_true(self):
        '''Testaa pelilogiikan funktiota is_board_full
        tapauksessa, jossa lauta on täynnä'''
        board = [[1, 1, 2, 1, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1]]
        is_full = self.game.is_board_full(board)
        self.assertEqual(is_full, True)

    def test_is_board_full_false(self):
        '''Testaa pelilogiikan funktiota is_board_full
        tapauksessa, jossa lauta ei ole täynnä'''
        board = [[1, 1, 2, 0, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [0, 2, 2, 1, 1, 2, 1]]
        is_full = self.game.is_board_full(board)
        self.assertEqual(is_full, False)

    def test_is_column_full_true(self):
        '''Testaa pelilogiikan funkiota is_column_full
        tapauksessa, jossa annettu sarake on täynnä'''
        board = [[0, 1, 2, 0, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1]]
        is_full = self.game.is_column_full(board, 1) #toinen sarake
        self.assertEqual(is_full, True)

    def test_is_column_full_false(self):
        '''Testaa pelilogiikan funkiota is_column_full
        tapauksessa, jossa annettu sarake ei ole täynnä'''
        board = [[1, 1, 2, 0, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [0, 2, 2, 1, 1, 2, 1]]
        is_full = self.game.is_column_full(board, 0) #ensimmäinen sarake
        self.assertEqual(is_full, False)

    def test_check_if_four_when_four_twos(self):
        '''Testaa pelilogiikan funkiota check_if_four,
        kun annettu rivi neljä kakkosta'''
        line = [2, 2, 2, 2] #neljä kakkosta
        check = self.game.check_if_four(line)
        self.assertEqual(2, check)

    def test_check_if_four_when_four_ones(self):
        '''Testaa pelilogiikan funkiota check_if_four,
        kun annettu rivi neljä ykköstä'''
        line = [1, 1, 1, 1] #neljä ykköstä
        check = self.game.check_if_four(line)
        self.assertEqual(1, check)

    def test_check_if_not_four(self):
        '''Testaa pelilogiikan funkiota check_if_four,
        kun annetussa rivissä ei ole neljää samaa'''
        line = [0, 1, 2, 0] #neljä kakkosta
        check = self.game.check_if_four(line)
        self.assertEqual(-1, check)

    def test_horizontal_win_for_player_two(self):
        '''Testaa vaakatasoisen voiton pelaajalle 2'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 2, 1, 0],
                 [0, 2, 2, 2, 2, 1, 0]]
        returns_2 = self.game.check_horizontal_win(board)
        self.assertEqual(returns_2, 2)

    def test_horizontal_win_for_player_one(self):
        '''Testaa vaakatasoisen voiton pelaajalle 1'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_1 = self.game.check_horizontal_win(board)
        self.assertEqual(returns_1, 1)

    def test_no_horizontal_win(self):
        '''Testaa, että funktio check_horizontal_win
        palauttaa 0, kun ei voittoa'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_0 = self.game.check_horizontal_win(board)
        self.assertEqual(returns_0, 0)

    def test_vertical_win_for_player_2(self):
        '''Testaa pystysyyntaisen voiton pelaajalle 2'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0],
                 [0, 2, 1, 0, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_2 = self.game.check_vertical_win(board)
        self.assertEqual(returns_2, 2)

    def test_vertical_win_for_player_1(self):
        '''Testaa pystysyyntaisen voiton pelaajalle 1'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 2, 1, 0, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_1 = self.game.check_vertical_win(board)
        self.assertEqual(returns_1, 1)

    def test_no_vertical_win(self):
        '''Testaa, että funktio check_vertical_win
        palauttaa 0 kun ei voittoa'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 2, 1, 0, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_0 = self.game.check_vertical_win(board)
        self.assertEqual(returns_0, 0)

    def test_diagonal_win_upwards_for_player_2(self):
        '''Testaa voiton yläviistoon pelaajalle 2'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [0, 2, 2, 1, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_2 = self.game.check_diagonal_up(board)
        self.assertEqual(returns_2, 2)

    def test_diagonal_win_upwards_for_player_1(self):
        '''Testaa voiton yläviistoon pelaajalle 1'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 2, 2, 1, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 1, 1, 2, 2, 1, 0]]
        returns_1 = self.game.check_diagonal_up(board)
        self.assertEqual(returns_1, 1)

    def test_diagonal_win_upwards_when_no_win(self):
        '''Testaa, että funktio palauttaa 0,
        tilanteessa, jossa ei voittoa'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 2, 2, 1, 1, 2, 0],
                 [1, 2, 1, 1, 2, 1, 0],
                 [2, 1, 1, 2, 2, 1, 0]]
        returns_0 = self.game.check_diagonal_up(board)
        self.assertEqual(returns_0, 0)

    def test_diagonal_win_downwards_for_player_2(self):
        '''Testaa voiton alaviistoon pelaajalle 2'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 2, 0, 0, 0],
                 [0, 1, 2, 1, 1, 2, 0],
                 [1, 1, 1, 2, 2, 1, 0],
                 [2, 2, 1, 2, 2, 1, 0]]
        returns_2 = self.game.check_diagonal_down(board)
        self.assertEqual(returns_2, 2)

    def test_diagonal_win_downwards_for_player_1(self):
        '''Testaa voiton alaviistoon pelaajalle 1'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 2, 0, 0, 0],
                 [2, 1, 2, 1, 1, 2, 0],
                 [1, 1, 1, 2, 2, 1, 0],
                 [2, 2, 1, 1, 2, 1, 0]]
        returns_1 = self.game.check_diagonal_down(board)
        self.assertEqual(returns_1, 1)

    def test_diagonal_win_downwards_when_no_win(self):
        '''Testaa, että funktio palauttaa 0,
        tilanteessa, jossa ei voittoa'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [2, 1, 2, 1, 1, 2, 0],
                 [1, 1, 1, 2, 2, 1, 0],
                 [2, 2, 1, 1, 2, 1, 0]]
        returns_0 = self.game.check_diagonal_down(board)
        self.assertEqual(returns_0, 0)

    def test_win_for_player_2(self):
        '''Testaa funktiota check_win(),
        kun pelaaja 2 on voittaja'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [2, 1, 2, 1, 1, 2, 0],
                 [1, 2, 1, 2, 2, 1, 0],
                 [2, 2, 1, 1, 2, 1, 0]]
        returns_2 = self.game.check_win(board)
        self.assertEqual(returns_2, 2)

    def test_win_for_player_1(self):
        '''Testaa funktiota check_win(),
        kun pelaaja 1 on voittaja'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [2, 1, 0, 0, 0, 2, 0],
                 [1, 1, 1, 1, 2, 1, 0],
                 [2, 2, 1, 1, 2, 1, 0]]
        returns_1 = self.game.check_win(board)
        self.assertEqual(returns_1, 1)

    def test_no_win(self):
        '''Testaa, että funktio check_win()
        palauttaa 0, kun ei voittoa'''
        board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [2, 1, 0, 0, 0, 2, 0],
                 [1, 1, 1, 2, 2, 1, 0],
                 [2, 2, 1, 1, 2, 1, 0]]
        returns_0 = self.game.check_win(board)
        self.assertEqual(returns_0, 0)
