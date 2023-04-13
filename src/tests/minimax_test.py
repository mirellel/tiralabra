import unittest
import os
from files.minimax import Minimax
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMinimax(unittest.TestCase):
    def setUp(self):
        self.board = [[0, 1, 2, 2, 1, 0, 0],
                     [0, 1, 1, 2, 1, 0, 0],
                     [0, 0, 1, 1, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.minimax = Minimax()
        
    def test_best_move(self):
        board = ([[0, 1, 2, 2, 1, 0, 0],
                     [0, 1, 1, 2, 1, 0, 0],
                     [0, 0, 1, 2, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual((3, 3), self.minimax.best_move(board, 1))

    def test_count_three_twos(self):
        line = [0, 2, 2, 2]
        self.assertEqual(10, self.minimax.count_three(line))

    def test_count_four_ones(self):
        line = [1, 1, 1, 1]
        self.assertEqual(-1000, self.minimax.count_four(line))

    def test_score_diag_d_four(self):
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 1, 2, 2, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), -1000)

    def test_score_diag_u_four(self):
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 0, 2, 2, 1, 0, 0],
                 [0, 2, 1, 1, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), 1000)

    def test_score_hor_four(self):
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 2, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), 1000)

    def test_score_vert_four(self):
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 1, 2, 0, 2, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), -1000)
    
    def test_block_winning(self):
        board = [[0, 1, 2, 2, 1, 0, 0],
                 [0, 1, 1, 2, 1, 0, 0],
                 [0, 0, 1, 1, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual((3,4), self.minimax.best_move(board, 2))