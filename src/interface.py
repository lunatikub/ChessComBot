"""
Interface with the chess.com website.
Allows finding the chessboard on the screen.
Enables piece recognition on the board.
Allows making moves.
"""

from board import (
    FILES_MAP, REVERSE_FILES_MAP,
    RANKS_MAP, REVERSE_RANKS_MAP,
)


class Interface():

    def __init__(self, x1, y1, x2, y2):
        self.x = x1
        self.y = y1
        self.w = x2 - x1  # board width
        self.h = y2 - y1  # board height
        self.sw = self.w / 8  # square width
        self.sh = self.h / 8  # square height
        self.half_sw = self.sw / 2
        self.half_sh = self.sh / 2

    def get_coord_from_square(self, square):
        f = square[0]  # file
        r = square[1]  # rank
        x = int(self.sw * FILES_MAP[f] + self.half_sw)
        y = int(self.sh * RANKS_MAP[r] + self.half_sh)
        return x, y

    def get_square_from_coord(self, x, y):
        f = REVERSE_FILES_MAP[x // self.sw]
        r = REVERSE_RANKS_MAP[y // self.sh]
        return f + r
