'''Moduuli, joka sisältää testiluokan TestGameRun'''
import unittest
import os
from files.game_runner import Game
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestGameRun(unittest.TestCase):
    '''Testiluokka Game luokalle'''
    def setUp(self):
        '''set up'''
        self.game = Game()
        self.empty_board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

    def test_starting_attributes(self):
        '''testaa, onko attribuutit aluksi oikein'''
        board = self.empty_board
        running = False
        game_over = False
        tie = False
        green_win = False
        red_win = False
        green_turn = True
        ai_player = False
        turns = 0
        opponent = "player"

        self.assertEqual((board, running, game_over, tie, green_win,
                          red_win, green_turn, ai_player, turns, opponent),
                          (self.game.board, self.game.running, self.game.game_over,
                           self.game.game_tie, self.game.green_win,
                           self.game.red_win, self.game.green_turn,
                           self.game.ai_player, self.game.turns, self.game.opponent))


    def test_drop_piece(self):
        '''Testaa funktiota drop_piece'''
        self.game.board = self.empty_board
        self.game.drop_piece(0, 4, 1)
        self.assertEqual(self.game.board[0][4], 1)
        self.assertEqual(self.game.turns, 1)

    def test_turns_grow_by_one_after_each_move(self):
        '''Testaa, että self.turns kasvaa jokaisen siirron jälkeen'''
        self.game.board = self.empty_board
        self.game.drop_piece(0, 0, 1)
        self.game.drop_piece(0, 1, 2)
        self.game.drop_piece(0, 2, 1)
        self.game.drop_piece(0, 3, 2)
        self.assertEqual(self.game.turns, 4)

    def test_full_column(self):
        self.game.board = [[0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0]]
        full = self.game.full_column(3)
        not_full = self.game.full_column(4)
        self.assertEqual(full, True)
        self.assertEqual(not_full, False)

    def test_check_victory_for_player_1(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [1, 1, 1, 1, 0, 0, 0]]
        winner = self.game.check_victory()
        self.assertEqual((winner, self.game.green_win), (1, True))

    def test_check_victory_for_player_2(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 2, 0, 0, 0],
                           [0, 0, 2, 2, 0, 0, 0],
                           [0, 2, 1, 1, 0, 0, 0],
                           [2, 1, 1, 1, 0, 0, 0]]
        winner = self.game.check_victory()
        self.assertEqual((winner, self.game.red_win), (2, True))

    def test_check_victory_when_no_win(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 2, 2, 0, 0, 0],
                           [0, 2, 1, 1, 0, 0, 0],
                           [2, 1, 1, 1, 0, 0, 0]]
        winner = self.game.check_victory()
        self.assertEqual(winner, 0)

    def test_check_tie(self):
        self.game.board = [[1, 1, 2, 1, 2, 1, 1],
                           [2, 1, 2, 1, 2, 2, 2],
                           [1, 2, 1, 1, 1, 2, 1],
                           [1, 2, 2, 2, 1, 2, 1],
                           [1, 2, 1, 1, 2, 1, 1],
                           [2, 1, 1, 2, 0, 2, 2]]
        self.game.turns = 41
        self.game.drop_piece(5, 4, 2)
        self.game.check_tie()
        self.assertEqual(self.game.game_tie, True)
        self.assertEqual(self.game.game_over, True)

    def test_check_tie_false(self):
        self.game.board = [[1, 1, 2, 1, 2, 1, 1],
                           [2, 1, 2, 1, 2, 2, 2],
                           [1, 2, 1, 1, 1, 2, 1],
                           [1, 2, 2, 2, 1, 2, 1],
                           [1, 2, 1, 1, 2, 1, 1],
                           [2, 1, 1, 2, 0, 2, 2]]
        self.game.turns = 41
        tie = self.game.check_tie()
        self.assertEqual(tie, False)

    def test_get_empty_row(self):
        self.game.board = [[0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 2, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0]]
        row = self.game.get_empty_row(3)
        self.assertEqual(row, 5)

    def test_get_empty_row_when_column_is_full(self):
        self.game.board = [[0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0]]
        row = self.game.get_empty_row(2)
        self.assertEqual(row, -1)

    def test_restart(self):
        self.game.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 2, 0, 0, 0],
                           [0, 0, 2, 2, 0, 0, 0],
                           [0, 2, 1, 1, 0, 0, 0],
                           [2, 1, 1, 1, 0, 0, 0]]
        self.game.running = True
        self.game.game_over = True
        self.game.tie = False
        self.game.green_win = False
        self.game.red_win = True
        self.game.green_turn = False
        self.game.ai_player = True
        self.game.turns = 8
        self.game.restart()
        self.assertEqual((self.game.board, self.game.running, self.game.game_over,
                           self.game.game_tie, self.game.green_win,
                           self.game.red_win, self.game.green_turn,
                           self.game.ai_player, self.game.turns),
                           (self.empty_board, False, False, False,
                            False, False, True, False, 0))

    def test_handle_player_move_for_green_player(self):
        self.game.board = self.empty_board
        column = 3
        self.game.green_turn = True
        board_after_move = [[0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]
        move = self.game.handle_player_move(column)
        self.assertEqual(move, board_after_move)

    def test_handle_player_move_for_red_player(self):
        self.game.board = self.empty_board
        column = 3
        self.game.green_turn = False
        board_after_move = [[0, 0, 0, 2, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]
        move = self.game.handle_player_move(column)
        self.assertEqual(move, board_after_move)

    def test_handle_player_move_when_given_column_is_full(self):
        self.game.board = [[0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0]]
        column = 3
        self.game.green_turn = True
        board_after_move = [[0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0]]
        move = self.game.handle_player_move(column)
        self.assertEqual(move, board_after_move)

    def test_handle_ai_move(self):
        self.game.board = [[0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]
        self.game.green_turn = False
        self.game.game_over = False
        self.game.depth = 2
        move = self.game.handle_ai_move()
        board_after_move = [[0, 0, 2, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(move, board_after_move)
