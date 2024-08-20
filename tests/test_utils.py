import cv2

from utils import parse_move
from interface import get_board_coord


def test_parse_move():
    from_square, to_square = parse_move("e2e4")
    assert from_square == "e2" and to_square == "e4"

    from_square, to_square = parse_move("Ke2-e4")
    assert from_square == "e2" and to_square == "e4"

    from_square, to_square = parse_move("Ke2-e4Q")
    assert from_square == "e2" and to_square == "e4"


def test_get_borad_coord():
    img  = cv2.imread("tests/fullscreen.png")
    x1, y1, x2, y2 = get_board_coord(img)
    assert x1 == 491 and y1 == 208
    assert x2 == 1043 and y2 == 1009
