import cv2

from board import Board
from interface import Interface
from pieces import (
    ep,
    BR, BN, BB, BQ, BK, BP,
    WR, WN, WB, WQ, WK, WP,
)
from recognition import normalize, recognize


def test_recognize():
    img_board = cv2.imread("tests/recognition.png")
    h, w, _ = img_board.shape
    interface = Interface(0, 0, w, h)
    img_board = normalize(img_board)
    board = recognize(interface, img_board)
    assert board.b == [
        [BR, ep, BB, BQ, BK, BB, BN, BR],
        [BP, BP, ep, BP, BP, BP, BP, BP],
        [ep, ep, BN, ep, ep, ep, ep, ep],
        [ep, ep, BP, ep, ep, ep, ep, ep],
        [ep, ep, ep, ep, WP, ep, ep, ep],
        [ep, ep, WN, ep, ep, ep, ep, ep],
        [WP, WP, WP, WP, ep, WP, WP, WP],
        [WR, ep, WB, WQ, WK, WB, WN, WR],
    ]


def test_recognize_2():
    img_board = cv2.imread("tests/recognition_2.png")
    h, w, _ = img_board.shape
    interface = Interface(0, 0, w, h)
    img_board = normalize(img_board)
    board = recognize(interface, img_board)
    assert board.b == [
        [BR, BN, BB, BQ, BK, BB, ep, BR],
        [BP, ep, ep, BP, ep, ep, ep, BP],
        [ep, BP, ep, ep, ep, BP, BP, ep],
        [ep, WB, BP, ep, WN, ep, ep, ep],
        [ep, WP, ep, ep, WN, ep, ep, ep],
        [ep, ep, ep, WP, ep, ep, ep, ep],
        [WP, ep, WP, ep, ep, WP, WP, WP],
        [WR, ep, WB, WQ, WK, ep, ep, WR],
    ]
