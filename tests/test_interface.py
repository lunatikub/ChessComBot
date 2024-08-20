import cv2

from board import RANKS_MAP, FILES_MAP
from interface import Interface


def check_coord_bounds(interface, hs, ws, move):
    x, y = interface.get_coord_from_square(move)
    f = move[0]
    r = move[1]

    lx = FILES_MAP[f] * ws
    hx = (FILES_MAP[f] + 1) * ws
    ly = RANKS_MAP[r] * hs
    hy = (RANKS_MAP[r] + 1) * hs

    assert x > lx and x < hx and y > ly and y < hy


def test_get_coord_from_square():
    board = cv2.imread("tests/recognition.png")
    h, w, _ = board.shape
    interface = Interface(0, 0, w, h)
    hs = h / 8
    ws = w / 8
    check_coord_bounds(interface, hs, ws, "h5")
    check_coord_bounds(interface, hs, ws, "e2")
    check_coord_bounds(interface, hs, ws, "a8")
    check_coord_bounds(interface, hs, ws, "h1")
