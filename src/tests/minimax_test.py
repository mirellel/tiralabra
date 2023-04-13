'''Moduuli, joka sisältää testiluokan TestMinimax'''
import unittest
import os
from files.minimax import Minimax
os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMinimax(unittest.TestCase):
    '''Luokka, joka testaa minimax luokan ja algoritmin toimintaa'''
    def setUp(self):
        '''Alustaa attribuutit'''
        self.board = [[0, 1, 2, 2, 1, 0, 0],
                     [0, 1, 1, 2, 1, 0, 0],
                     [0, 0, 1, 1, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.minimax = Minimax()

    def test_best_move(self):
        '''Algortimi osaa sijoittaa parhaimman siirron'''
        board = ([[0, 1, 2, 2, 1, 0, 0],
                     [0, 1, 1, 2, 1, 0, 0],
                     [0, 0, 1, 2, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual((3, 3), self.minimax.best_move(board, 1))

    def test_count_three_twos(self):
        '''funktio palauttaa oikean arvon, kun
        suoralla on kolme kakkosta'''
        line = [0, 2, 2, 2]
        self.assertEqual(10, self.minimax.count_three(line))

    def test_count_four_ones(self):
        '''funktio palauttaa oikean arvon, kun
        suoralla on kolme ykköstä'''
        line = [1, 1, 1, 1]
        self.assertEqual(-1000, self.minimax.count_four(line))

    def test_score_diag_d_four(self):
        '''funktio palauttaa oikean arvon, kun
        alaspäin viistoon olevalla suoralla on
        neljä ykköstä'''
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 1, 2, 2, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), -1000)

    def test_score_diag_u_four(self):
        '''funktio palauttaa oikean arvon, kun
        alaspäin viistoon olevalla suoralla on
        neljä kakkosta'''
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 0, 2, 2, 1, 0, 0],
                 [0, 2, 1, 1, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), 1000)

    def test_score_hor_four(self):
        '''funktio palauttaa oikean arvon, kun
        vaakatasoisella suoralla on neljä kakkosta'''
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 2, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), 1000)

    def test_score_vert_four(self):
        '''funktio palauttaa oikean arvon, kun
        pystytasoisella suoralla on neljä ykköstä'''
        board = [[1, 1, 2, 2, 1, 0, 0],
                 [0, 1, 2, 0, 2, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.minimax.score(board), -1000)

    def test_block_winning(self):
        '''algoritmi osaa blokata pelaajan 1 mahdollisen
        voiton'''
        board = [[0, 1, 2, 2, 1, 0, 0],
                 [0, 1, 1, 2, 1, 0, 0],
                 [0, 0, 1, 1, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual((3,4), self.minimax.best_move(board, 2))
