'''Moduuli joka sisältää testiluokan TestMultiPlayer'''
import unittest
import os
from files.game import MainGame
from files.two_player import MultiPlayer
os.environ["SDL_VIDEODRIVER"] = "dummy"


class TestMultiplayer(unittest.TestCase):
    '''Testiluokka, joka testaa luokkaa MultiPlayer'''
    def setUp(self):
        '''Asettaa atribuutit'''
        self.game = MultiPlayer()
        self.game_logic = MainGame()
        self.empty_board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

    def test_drop_piece(self):
        '''Testaa funktiota drop_piece()'''
        board = self.game_logic.create_board(6, 7)
        player = 1
        row = 0
        column = 3
        self.game.drop_piece(board, row, column, player)
        test_board = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(test_board, board)

    def test_restart(self):
        '''Testaa funktiota restart()'''
        self.game.board = [[0, 0, 1, 1, 2, 2, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.game.running = True
        self.game.game_over = False
        self.game.mouse_position = (100, 700)
        self.game.green_turn = False
        self.game.green_win = False
        self.game.red_win = False

        self.game.restart()
        self.assertEqual((self.game.board, self.game.running, self.game.game_over,
                          self.game.mouse_position,
                          self.game.green_turn, self.game.green_win,
                          self.game.red_win),
                          (self.empty_board, False, False, (0, 0),
                           True, False, False))

    def test_get_empty_row(self):
        '''Testaa funktiota get_empty_row()'''
        board = [[1, 1, 2, 1, 2, 2, 1],
                 [2, 1, 1, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        column = 1
        correct_row = 2
        row = self.game.get_empty_row(board, column)
        self.assertEqual(row, correct_row)


    def test_full_column_true(self):
        '''Testaa funktiota full_column() tapauksessa, jossa
        sarake on täysi'''
        self.game.board =[[1, 1, 2, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [0, 2, 2, 0, 1, 2, 1]]
        is_full = self.game.full_column(1)
        self.assertEqual(is_full, True)

    def test_full_column_false(self):
        '''Testaa funktiota full_column() tapauksessa, jossa
        sarake ei ole täysi'''
        self.game.board =[[1, 1, 2, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [0, 2, 2, 0, 1, 2, 1]]
        is_full = self.game.full_column(0)
        self.assertEqual(is_full, False)

    def test_check_victory_1(self):
        '''Testaa funktiota check_victory(),
        kun pelaaja 1 on voittanut'''
        self.game.board = [[1, 1, 2, 1, 2, 2, 1],
                        [2, 1, 1, 2, 0, 0, 0],
                        [0, 1, 2, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        winner = self.game.check_victory()
        self.assertEqual((winner, self.game.green_win, self.game.game_over),
                         (1, True, True))

    def test_check_victory_2(self):
        '''Testaa funktiota check_victory(),
        kun pelaaja 1 on voittanut'''
        self.game.board = [[1, 2, 1, 1, 2, 1, 1],
                        [2, 2, 1, 2, 0, 0, 0],
                        [0, 2, 1, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        winner = self.game.check_victory()
        self.assertEqual((winner, self.game.red_win, self.game.game_over),
                         (2, True, True))

    def test_check_tie(self):
        '''Testaa funktiota check_tie()'''
        self.game.board = [[1, 1, 2, 2, 2, 1, 2],
                           [1, 2, 2, 1, 1, 2, 1],
                           [2, 1, 2, 2, 2, 1, 2],
                           [2, 1, 1, 1, 2, 1, 2],
                           [2, 2, 1, 2, 2, 1, 2],
                           [1, 2, 2, 1, 1, 2, 1]]
        self.game.game_over = False
        self.game.check_tie()
        self.assertEqual(self.game.game_over, True)

    def test_handle_player_move_1(self):
        '''Testaa funktiota handle_player_move(),
        pelaajan 1 siirron jälkeen'''
        self.game.board = self.empty_board
        board_after_move = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.game.green_turn = True
        column = 3
        board = self.game.handle_player_move(column)
        self.assertEqual(board, board_after_move)

    def test_handle_player_move_2(self):
        '''Testaa funktiota handle_player_move(),
        pelaajan 2 siirron jälkeen'''
        self.game.board = self.empty_board
        board_after_move = [[0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.game.green_turn = False
        column = 3
        board = self.game.handle_player_move(column)
        self.assertEqual(board, board_after_move)
