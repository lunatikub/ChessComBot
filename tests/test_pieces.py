from pieces import (
    PieceType,
    PieceColor,
    BR, BN, BB, BQ, BK, BP,
    WR, WN, WB, WQ, WK, WP,
)


def test_pieces():
    assert BR.type == PieceType.ROOK and BR.color == PieceColor.BLACK
    assert BN.type == PieceType.KNIGHT and BR.color == PieceColor.BLACK
    assert BB.type == PieceType.BISHOP and BR.color == PieceColor.BLACK
    assert BQ.type == PieceType.QUEEN and BR.color == PieceColor.BLACK
    assert BK.type == PieceType.KING and BR.color == PieceColor.BLACK
    assert BP.type == PieceType.PAWN and BR.color == PieceColor.BLACK

    assert WR.type == PieceType.ROOK and WR.color == PieceColor.WHITE
    assert WN.type == PieceType.KNIGHT and WR.color == PieceColor.WHITE
    assert WB.type == PieceType.BISHOP and WR.color == PieceColor.WHITE
    assert WQ.type == PieceType.QUEEN and WR.color == PieceColor.WHITE
    assert WK.type == PieceType.KING and WR.color == PieceColor.WHITE
    assert WP.type == PieceType.PAWN and WR.color == PieceColor.WHITE
