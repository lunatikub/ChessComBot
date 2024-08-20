"""
A chess piece, or chessman, is a game piece that is placed
on a chessboard to play the game of chess. It can be either
white or black, and it can be one of six types:
king, queen, rook, bishop, knight, or pawn.
Each piece is associated with a template to recognize it on a board.
"""

import cv2

from enum import Enum
from pathlib import Path


class PieceColor(Enum):
    NONE = "none"
    WHITE = "white"
    BLACK = "black"


class PieceType(Enum):
    NONE = "none"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"
    PAWN = "pawn"


class Piece():
    def __init__(self,
                 color: PieceColor,
                 type: PieceType,
                 repr: str):
        self.color = color
        self.type = type
        self.repr = repr
        self.template = self._template()

    def __str__(self) -> str:
        return self.repr

    def _template(self):
        if self.type == PieceType.NONE:
            return ""
        filepath = Path("templates", f"{self.color.value}_{self.type.value}.png")
        print(filepath.absolute())
        assert filepath.exists(), f"File {filepath} doesn't exist..."
        template = cv2.imread(filepath)
        return cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    def __eq__(self, other):
        return self.color == other.color and self.type == other.type


ep = Piece(PieceColor.NONE, PieceType.NONE, ".") # empty square
BR = Piece(PieceColor.BLACK, PieceType.ROOK, "r")
BN = Piece(PieceColor.BLACK, PieceType.KNIGHT, "n")
BB = Piece(PieceColor.BLACK, PieceType.BISHOP, "b")
BQ = Piece(PieceColor.BLACK, PieceType.QUEEN, "q")
BK = Piece(PieceColor.BLACK, PieceType.KING, "k")
BP = Piece(PieceColor.BLACK, PieceType.PAWN, "p")
WR = Piece(PieceColor.WHITE, PieceType.ROOK, "R")
WN = Piece(PieceColor.WHITE, PieceType.KNIGHT, "N")
WB = Piece(PieceColor.WHITE, PieceType.BISHOP, "B")
WQ = Piece(PieceColor.WHITE, PieceType.QUEEN, "Q")
WK = Piece(PieceColor.WHITE, PieceType.KING, "K")
WP = Piece(PieceColor.WHITE, PieceType.PAWN, "P")

PIECES = [BR, BN, BB, BQ, BK, BP, WR, WN, WB, WQ, WK, WP]
