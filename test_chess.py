import unittest
from chess import Chess

class TestChess(unittest.TestCase):
    def test_board_initialization(self):
        chess = Chess()
        self.assertEqual(chess.board[0][0], 'R')
        self.assertEqual(chess.board[0][4], 'K')
        self.assertEqual(chess.board[1][0], 'P')
        self.assertEqual(chess.board[7][0], 'r')
        self.assertEqual(chess.board[7][4], 'k')
        self.assertEqual(chess.board[6][0], 'p')
        self.assertIsNone(chess.board[3][3])

    def test_turn_initialization(self):
        chess = Chess()
        self.assertEqual(chess.turn, 'w')

    def test_history_initialization(self):
        chess = Chess()
        self.assertEqual(chess.history, [])

if __name__ == '__main__':
    unittest.main()
