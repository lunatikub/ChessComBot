import copy

from board import Board
from pieces import (
    ep,
    BR, BN, BB, BQ, BK, BP,
    WR, WN, WB, WQ, WK, WP,
)


def test_nominal_move():
    b = Board()
    b.reset()
    b.move("e2e4")
    b.move("c7c5")
    b.move("g1f3")
    b.move("g7g6")
    b.move("f3d4")
    b.move("c5d4")
    b.b == [
        [BR, BN, BB, BQ, BK, BB, BN, BR],
        [BP, BP, ep, BP, BP, BP, ep, BP],
        [ep, ep, ep, ep, ep, ep, BP, ep],
        [ep, ep, ep, ep, ep, ep, ep, ep],
        [ep, ep, ep, BP, WP, ep, ep, ep],
        [ep, ep, ep, ep, ep, ep, ep, ep],
        [WP, WP, WP, WP, ep, WP, WP, WP],
        [WR, WN, WB, WQ, WK, WB, ep, WR],
    ]


def test_get_nominal_move_from_diff():
    b1 = Board()
    b1.reset()
    b2 = copy.deepcopy(b1)
    b2.move("e2e4")
    diff = b1.diff(b2)
    move = b1.get_move_from_diff(diff)
    assert move == "e2e4"


def test_get_capturing_move_from_diff():
    b1 = Board()
    b1.reset()
    b1.move("e2e4")
    b1.move("c7c5")
    b1.move("g1f3")
    b1.move("g7g6")
    b1.move("f3d4")
    b2 = copy.deepcopy(b1)
    b2.move("c5d4")
    diff = b1.diff(b2)
    move = b1.get_move_from_diff(diff)
    assert move == "c5d4"
