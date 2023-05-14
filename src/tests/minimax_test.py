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
        correct_score = 100
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

    def test_defend_when_opponent_wins(self):
        '''Testaa löytääkö algoritmi parhaan siirron,
        kun vastustajalla on kolmen suora'''
        self.board = [[1, 1, 2, 1, 2, 1, 1],
                      [0, 2, 1, 2, 1, 2, 0],
                      [0, 0, 0, 1, 1, 0, 0],
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
        board = [[1, 2, 2, 1, 1, 1, 2],
                 [1, 0, 1, 2, 1, 0, 2],
                 [1, 0, 2, 2, 2, 0, 2],
                 [2, 0, 1, 1, 2, 0, 1],
                 [2, 0, 1, 2, 2, 0, 2],
                 [1, 0, 1, 2, 1, 0, 1]]
        depth = 2
        col = self.minimax.minimax(board, depth, True)[0]
        # minimax käy sarakkeet läpi aina järjestyksessä 3, 2, 4, 1, 5, 0, 6
        # joten algoritmi löytää parhaimman siirron sarakkeesta 1, vaikka
        # siirto sarakkeeseen 5 on yhtä hyvä
        self.assertEqual(col, 1)
        board[1][col]=2
        board[2][col]=1
        col2=self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col2, 1)
        board[3][col2] = 2
        winner = self.minimax.check_win(board)
        self.assertEqual(winner, 2)

    def test_find_win_in_five_moves_depth_5(self):
        board = ([
            [1, 1, 2, 1, 2, 0, 1],
            [0, 1, 2, 2, 1, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [0, 1, 2, 1, 1, 0, 0],
            [0, 1, 1, 1, 2, 0, 0]
        ])
        # sarakkeesta 6 saadaan välttämättä voitto
        # joka löytyy syvyydellä 5
        depth = 5
        col = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col, 5)
        board[0][col]=2
        board[1][5]=1
        col2 = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col2, 5)
        board[2][col2] = 2
        board[1][6] = 1
        col3 = self.minimax.minimax(board, 5, True)[0]
        self.assertEqual(col3, 5)
        board[3][col3] = 2
        winner = self.minimax.check_win(board)
        self.assertEqual(winner, 2)

        board = ([
            [1, 1, 2, 1, 2, 0, 1],
            [0, 1, 2, 2, 1, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [0, 2, 1, 2, 2, 0, 0],
            [0, 1, 2, 1, 1, 0, 0],
            [0, 1, 1, 1, 2, 0, 0]
        ])

        #voitto ei löydy syvyydellä 2
        col4 = self.minimax.minimax(board, 2, True)[0]
        self.assertNotEqual(col4, col)

    def test_find_win_in_three_moves_depth_3(self):
        board = ([
            [0, 1, 2, 1, 1, 1, 2],
            [0, 1, 1, 2, 0, 1, 1],
            [0, 2, 2, 2, 0, 2, 1],
            [0, 1, 1, 2, 0, 2, 2],
            [0, 0, 1, 1, 0, 1, 2],
            [0, 0, 2, 2, 0, 2, 1]
        ])
        # sarakkeesta 5 saadaan voitto välttämättä
        # kolmen siirron jälkeen
        depth = 3
        col = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col, 4)
        board[1][col]=4
        board[4][6]=1
        col2 = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col2, 4)
        board[2][col2]=2
        winner = self.minimax.check_win(board)
        self.assertEqual(winner, 2)

        # voitto ei löydy syvyydellä 2
        board = ([
            [0, 1, 2, 1, 1, 1, 2],
            [0, 1, 1, 2, 0, 1, 1],
            [0, 2, 2, 2, 0, 2, 1],
            [0, 1, 1, 2, 0, 2, 2],
            [0, 0, 1, 1, 0, 1, 2],
            [0, 0, 2, 2, 0, 2, 1]
        ])
        col3 = self.minimax.minimax(board, 2, True)[0]
        self.assertNotEqual(col3, col)

    def test_find_win_in_six_moves_depth_6(self):
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
        board[0][col] = 2
        board[0][1] = 1
        col2 = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col2, 2)
        board[1][col2] = 2
        board[1][1] = 1
        col3 = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col3, 2)
        board[2][col3] = 2
        board[2][1] = 1
        col4 = self.minimax.minimax(board, depth, True)[0]
        self.assertEqual(col4, 2)
        board[3][col4] = 2
        winner = self.minimax.check_win(board)
        self.assertEqual(winner, 2)

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
