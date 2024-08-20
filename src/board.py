"""
A chessboard is a game board used to play chess.
It consists of 64 squares, 8 rows by 8 columns,
on which the chess pieces are placed.
"""

import numpy as np

from utils import parse_move

from pieces import (
    Piece, PieceColor, NP,
    BR, BN, BB, BQ, BK, BP,
    WR, WN, WB, WQ, WK, WP,
)

RANKS_MAP = {
    '1': 7, '2': 6, '3': 5, '4': 4,
    '5': 3, '6': 2, '7': 1, '8': 0,
}

REVERSE_RANKS_MAP = {
    7: '1', 6: '2', 5: '3', 4: '4',
    3: '5', 2: '6', 1: '7', 0: '8',
}

FILES_MAP = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3,
    'e': 4, 'f': 5, 'g': 6, 'h': 7
}

REVERSE_FILES_MAP = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd',
    4: 'e', 5: 'f', 6: 'g', 7: 'h',
}


def get_filerank(square):
    return FILES_MAP[square[0]], RANKS_MAP[square[1]]


class Board():

    def __init__(self):
        self.b = [
            [BR, BN, BB, BQ, BK, BB, BN, BR],
            [BP, BP, BP, BP, BP, BP, BP, BP],
            [NP, NP, NP, NP, NP, NP, NP, NP],
            [NP, NP, NP, NP, NP, NP, NP, NP],
            [NP, NP, NP, NP, NP, NP, NP, NP],
            [NP, NP, NP, NP, NP, NP, NP, NP],
            [WP, WP, WP, WP, WP, WP, WP, WP],
            [WR, WN, WB, WQ, WK, WB, WN, WR],
        ]

    def __str__(self):
        str = ""
        for i in range(len(self.b)):
            str += REVERSE_FILES_MAP[i]
        str += "\n--------\n"
        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                str += self.b[i][j].repr
            str += " |"
            str += REVERSE_RANKS_MAP[i]
            str += "\n"
        return str

    def move(self, move):
        """
        Move a piece on the board with a
        LAN (Long algebraic notation) notation.
        """
        from_square, to_square = parse_move(move)
        x1, y1 = get_filerank(from_square)
        x2, y2 = get_filerank(to_square)
        self.b[y2][x2] = self.b[y1][x1]
        self.b[y1][x1] = NP

    def diff(self, board):
        """
        Identify the differences between two chess boards.
        """
        b1 = np.array(self.b)
        b2 = np.array(board.b)
        diff = np.where(b1 != b2)
        differences = [(i, j, b1[i, j], b2[i, j]) for i, j in zip(diff[0], diff[1])]
        return differences

    def get_move_from_diff(self, diff):
        """
        Deduce a move from the difference between two boards.
        """
        assert len(diff) == 2
        for d in diff:
            if (d[3] == NP):
                from_square = REVERSE_FILES_MAP[d[1]] + REVERSE_RANKS_MAP[d[0]]
            else:
                to_square = REVERSE_FILES_MAP[d[1]] + REVERSE_RANKS_MAP[d[0]]
        return from_square + to_square
