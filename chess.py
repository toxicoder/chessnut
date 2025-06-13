class Chess:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'w'
        self.history = []

        # Place white pieces
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.board[1] = ['P' for _ in range(8)]

        # Place black pieces
        self.board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        self.board[6] = ['p' for _ in range(8)]
