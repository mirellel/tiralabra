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
        self.multiplayer = MultiPlayer()
        self.game = MainGame()
        self.empty_board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

    def test_drop_piece(self):
        '''Testaa funktiota drop_piece()'''
        board = self.game.create_board(6, 7)
        player = 1
        row = 0
        column = 3
        self.multiplayer.drop_piece(board, row, column, player)
        test_board = [[0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(test_board, board)

    def test_restart(self):
        '''Testaa funktiota restart()'''
        self.multiplayer.board = [[0, 0, 1, 1, 2, 2, 1],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.multiplayer.running = True
        self.multiplayer.game_over = False
        self.multiplayer.mouse_position = (100, 700)
        self.multiplayer.green_turn = False
        self.multiplayer.green_win = False
        self.multiplayer.red_win = False

        self.multiplayer.restart()
        self.assertEqual((self.multiplayer.board, self.multiplayer.running,
                          self.multiplayer.game_over,
                          self.multiplayer.mouse_position,
                          self.multiplayer.green_turn, self.multiplayer.green_win,
                          self.multiplayer.red_win),
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
        row = self.multiplayer.get_empty_row(board, column)
        self.assertEqual(row, correct_row)


    def test_full_column_true(self):
        '''Testaa funktiota full_column() tapauksessa, jossa
        sarake on täysi'''
        board =[[1, 1, 2, 2, 2, 1, 2],
                          [1, 2, 2, 1, 1, 2, 1],
                          [2, 1, 2, 2, 2, 1, 2],
                          [2, 1, 1, 1, 2, 1, 2],
                          [2, 2, 1, 2, 2, 1, 2],
                          [0, 2, 2, 0, 1, 2, 1]]
        is_full = self.multiplayer.full_column(1, board)
        self.assertEqual(is_full, True)

    def test_full_column_false(self):
        '''Testaa funktiota full_column() tapauksessa, jossa
        sarake ei ole täysi'''
        board =[[1, 1, 2, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [0, 2, 2, 0, 1, 2, 1]]
        is_full = self.multiplayer.full_column(0, board)
        self.assertEqual(is_full, False)

    def test_check_victory_1(self):
        '''Testaa funktiota check_victory(),
        kun pelaaja 1 on voittanut'''
        self.multiplayer.board = [[1, 1, 2, 1, 2, 2, 1],
                        [2, 1, 1, 2, 0, 0, 0],
                        [0, 1, 2, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        winner = self.multiplayer.check_victory()
        self.assertEqual((winner, self.multiplayer.green_win, self.multiplayer.game_over),
                         (1, True, True))

    def test_check_victory_2(self):
        '''Testaa funktiota check_victory(),
        kun pelaaja 1 on voittanut'''
        self.multiplayer.board = [[1, 2, 1, 1, 2, 1, 1],
                        [2, 2, 1, 2, 0, 0, 0],
                        [0, 2, 1, 0, 0, 0, 0],
                        [0, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        winner = self.multiplayer.check_victory()
        self.assertEqual((winner, self.multiplayer.red_win, self.multiplayer.game_over),
                         (2, True, True))

    def test_check_tie(self):
        '''Testaa funktiota check_tie()'''
        game_over = False
        tie = False
        self.multiplayer.board = [[1, 1, 2, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1],
                 [2, 1, 2, 2, 2, 1, 2],
                 [2, 1, 1, 1, 2, 1, 2],
                 [2, 2, 1, 2, 2, 1, 2],
                 [1, 2, 2, 1, 1, 2, 1]]
        self.multiplayer.check_tie(self.multiplayer.board)
        game_over = self.multiplayer.game_over
        tie = self.multiplayer.tie_game
        self.assertEqual((game_over, tie), (True, True))

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
        self.multiplayer.green_turn = True
        column = 3
        board = self.multiplayer.handle_player_move(column)
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
        self.multiplayer.green_turn = False
        column = 3
        board = self.multiplayer.handle_player_move(column)
        self.assertEqual(board, board_after_move)
