'''Moduuli joka sisältää testiluokan TestSinglePlayer'''
import unittest
import os
from files.game import MainGame
from files.singleplayer import SinglePlayer
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestSinglePlayer(unittest.TestCase):
    '''Testiluokka, joka testaa luokkaa MultiPlayer'''
    def setUp(self):
        '''Asettaa atribuutit'''
        self.game = SinglePlayer()
        self.game_logic = MainGame()
        self.empty_board = [[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]

    def test_if_ai_player_is_true(self):
        '''Tarkistaa, että ai_player on totta'''
        self.assertEqual(True, self.game.ai_player)

    def test_ai_makes_best_starting_move(self):
        '''Testaa, että ai tekee parhaimman siirron'''
        self.game.board = [[0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]
        self.game.ai_move()
        board_after_move = [[0, 0, 1, 2, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(board_after_move, self.game.board)

    def test_handle_player_move(self):
        '''Testaa funktion toimintaa'''
        self.game.board = self.empty_board
        board = self.game.handle_player_move(4)
        board_after_move = [[0, 0, 0, 2, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(board, board_after_move)
