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
    def test_rate_possible_move_for_player2_two(self):
        '''Testaa palauttaako rate_possible_move
        oikean arvon, kun siirrossa on kaksi kakkosta'''
        possible_move = [2, 2, 0, 0]
        piece = 2
        score = self.minimax.rate_possible_move(possible_move, piece)
        correct_score = 4
        self.assertEqual(score, correct_score)

    def test_rate_possible_move_for_player2_three(self):
        '''Testaa palauttaako rate_possible_move
        oikean arvon, kun siirrossa on kolme kakkosta'''
        possible_move = [2, 2, 2, 0]
        piece = 2
        score = self.minimax.rate_possible_move(possible_move, piece)
        correct_score = 10
        self.assertEqual(score, correct_score)

    def test_rate_possible_move_for_player2_four(self):
        '''Testaa palauttaako rate_possible_move
        oikean arvon, kun siirrossa on neljä kakkosta'''
        possible_move = [2, 2, 2, 2]
        piece = 2
        score = self.minimax.rate_possible_move(possible_move, piece)
        correct_score = 10
        self.assertEqual(score, correct_score)

    def test_rate_possible_move_for_player1_two(self):
        '''Testaa palauttaako rate_possible_move
        oikean arvon, kun siirrossa on kaksi ykköstä'''
        possible_move = [1, 1, 0, 0]
        piece = 2
        score = self.minimax.rate_possible_move(possible_move, piece)
        correct_score = -4
        self.assertEqual(score, correct_score)

    def test_rate_possible_move_for_player1_three(self):
        '''Testaa palauttaako rate_possible_move
        oikean arvon, kun siirrossa on kolme ykköstä'''
        possible_move = [1, 1, 1, 0]
        piece = 2
        score = self.minimax.rate_possible_move(possible_move, piece)
        correct_score = -10
        self.assertEqual(score, correct_score)

    def test_defend_possible_defeat(self):
        '''Tetsaa löytääkö algoritmi parhaan siirron,
        kun vastustajalla on kolmen suora'''
        board = self.board
        column = self.minimax.minimax(board, 2, True)[0]
        self.assertEqual(column, 4)

    def test_defend_when_opponent_wins_in_two_moves(self):
        '''Testaa löytääkö algoritmi parhaan siirron,
        kun vastustajalla on kahden suora'''
        self.board = [[1, 1, 2, 1, 2, 1, 1],
                      [0, 2, 0, 2, 1, 2, 0],
                      [0, 0, 0, 2, 1, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        depth = 2
        col = self.minimax.minimax(self.board, depth, True)[0]
        self.assertEqual(col, 4)

    def test_find_win_in_two_moves_depth_2(self):
        '''Testaa löytääkö algoritmi voittavan
        siirron syvyydellä 2 kun voitto on
        kahden siirron päässä'''
        self.board = [[1, 2, 2, 1, 1, 1, 2],
                      [1, 0, 1, 2, 1, 0, 2],
                      [1, 0, 2, 2, 2, 0, 2],
                      [2, 0, 1, 1, 2, 0, 1],
                      [2, 0, 1, 2, 2, 0, 2],
                      [1, 0, 1, 2, 1, 0, 1]]
        depth = 2
        col = self.minimax.minimax(self.board, depth, True)[0]
        # minimax käy sarakkeet läpi aina järjestyksessä 3, 2, 4, 1, 5, 0, 6
        # joten algoritmi löytää parhaimman siirron sarakkeesta 1, vaikka
        # siirto sarakkeeseen 5 on yhtä hyvä
        self.assertEqual(col, 1)

    def test_find_win_in_five_moves(self):
        board = ([
            [1, 1, 2, 1, 2, 0, 1],
            [0, 0, 2, 2, 1, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0]
        ])
        depth = 3
        col = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col, 5)

    def test_find_win_in_three_moves(self):
        board = ([
            [0, 1, 2, 1, 1, 1, 2],
            [0, 1, 1, 2, 0, 1, 1],
            [0, 2, 2, 2, 0, 2, 1],
            [0, 0, 2, 1, 0, 2, 0],
            [0, 0, 1, 2, 0, 1, 0],
            [0, 0, 2, 2, 0, 0, 0]
        ])
        depth = 3
        col = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col, 0)

    def test_find_win_in_six_moves(self):
        board = ([
            [2, 0, 0, 2, 1, 2, 1],
            [1, 0, 0, 1, 2, 1, 0],
            [2, 0, 0, 2, 1, 2, 0],
            [1, 0, 0, 2, 1, 1, 0],
            [2, 0, 0, 2, 2, 0, 0],
            [1, 0, 0, 1, 1, 0, 0]
        ])
        depth = 6
        col = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col, 2)

    def test_get_valid_locations(self):
        board = self.board
        valid_locations = self.minimax.get_valid_locations(board)
        self.assertEqual(valid_locations, [0, 1, 2, 3, 4, 5, 6])

    def test_score(self):
        self.board = [[0, 1, 2, 2, 1, 0, 0],
                      [0, 1, 1, 2, 1, 0, 0],
                      [0, 0, 1, 1, 2, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        piece = 2
        score = self.minimax.score(self.board, piece)
        # pisteet: keskellä on 2 kakkosta = 6 pistettä
        # kolme kakkosta oikealle viistoon = 10 pistettä
        # kaksi kakkosta oikealle viistoon = 4 pistettä
        # kolme ykköstä oikealle viistoon = -10 pistettä
        # kaksi ykköstä oikealle viistoon x3 = -8 pistettä
        # kaksi ykköstä vasemmalle viistoon x2 = -8 pistettä
        # kaksi ykköstä vaakarivillä = -4 pistettä
        # kaksi ykkösyä pystysuunnassa = -4 pistettä
        # 20 - 10 - 8 -8 - 4 - 4 -4 =  -18
        self.assertEqual(score, -18)
