import pyautogui
import cv2
import numpy as np


def parse_move(move):
    """
    Parse Long algebraic notation chess move.
    <LAN move descriptor piece moves> ::= <Piece symbol><from square>['-'|'x']<to square>
    <LAN move descriptor pawn moves>  ::= <from square>['-'|'x']<to square>[<promoted to>]
    <Piece symbol> ::= 'N' | 'B' | 'R' | 'Q' | 'K'
    """
    if (move.startswith("N") or move.startswith("B")
        or move.startswith("R") or move.startswith("Q")
        or move.startswith("K")):
        move = move[1:]
    from_square = move[0:2]
    move = move[2:]
    if (move.startswith("-") or move.startswith("x")):
        move = move[1:]
    to_square = move[0:2]
    return from_square, to_square


def _screenshot(img):
    # Convert the screenshot to a numpy array
    img_np = np.array(img)
    # OpenCV works with images in BGR format,
    # but pyautogui provides image in RGB format.
    # Convert the image from RGB to BGR format
    return cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)


def screenshot_full():
    return _screenshot(pyautogui.screenshot())


def screenshot_region(x, y, w, h):
    return _screenshot(pyautogui.screenshot(region=(x, y, w, h)))


