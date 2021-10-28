import unittest

import chess
import scorer

# thanks @jstrassburg
class TestScorer(unittest.TestCase):
    def setUp(self):
        self._scorer = scorer.Scorer()
        self._board = chess.Board()

    def test_default_board_is_not_end_game(self):
        expected = False
        actual = self._scorer._is_end_game(self._board)
        self.assertEqual(expected, actual)

    def test_no_queens_is_end_game(self):
        expected = True
        board = chess.Board(fen='rnb1kbnr/8/8/8/8/8/8/RNB1KBNR')
        actual = self._scorer._is_end_game(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_no_other_pieces_is_end_game(self):
        expected = True
        board = chess.Board(fen='7q/8/8/8/8/8/8/7K')
        actual = self._scorer._is_end_game(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_one_other_piece_is_end_game(self):
        expected = True
        board = chess.Board(fen='6rq/8/8/8/8/8/8/7K')
        actual = self._scorer._is_end_game(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_two_other_pieces_is_not_endgame(self):
        expected = False
        board = chess.Board(fen='4kbrq/8/8/8/8/8/8/7K')
        actual = self._scorer._is_end_game(board)
        self.assertEqual(expected, actual)

    def test_evaluate_initial_board(self):
        expected = 0
        actual = self._scorer.evaluate(self._board)
        self.assertEqual(expected, actual)

    def test_evaluate_first_move_e4(self):
        expected = 40
        self._board.push_san('e4')
        actual = self._scorer.evaluate(self._board)
        self.assertEqual(expected, actual)

    def test_evaluate_first_two_moves_pawns(self):
        expected = 0
        self._board.push_san('e4')
        self._board.push_san('e5')
        actual = self._scorer.evaluate(self._board)
        self.assertEqual(expected, actual)

    def test_evaluate_specific_board_middle_game(self):
        expected = 5
        board = chess.Board(fen='1kr5/q7/8/8/8/3Q4/8/K7')
        actual = self._scorer.evaluate(board)
        self.assertEqual(expected, actual)

    def test_evaluate_specific_board_end_game(self):
        expected = 90
        board = chess.Board(fen='k7/4R3/8/8/8/3K4/8/8')
        actual = self._scorer.evaluate(board)
        self.assertEqual(expected, actual)

    def test_evaluate_specific_board_black_ahead(self):
        expected = -95
        board = chess.Board(fen='8/8/3k4/2n5/8/8/8/7K')
        actual = self._scorer.evaluate(board)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
