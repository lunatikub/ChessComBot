"""
Interface with the chess.com website.
Allows finding the chessboard on the screen.
Enables piece recognition on the board.
Allows making moves.
"""

import cv2
import numpy as np
import pyautogui
import time

from board import (
    FILES_MAP, REVERSE_FILES_MAP,
    RANKS_MAP, REVERSE_RANKS_MAP,
)
from recognition import normalize
from utils import screenshot_region, parse_move


# BGR squares color on the chess.ocm website.
WHITE_SQUARE_COLOR = [208, 236, 235]
BLACK_SQUARE_COLOR = [82, 149, 115]
YELLOW1_SQUARE_COLOR = [67, 202, 185]
YELLOW2_SQUARE_COLOR = [130, 246, 245]


def diff_board(b1, b2):
    """
    Detect a difference between two boards.
    """
    b1 = cv2.resize(b1, (b2.shape[1], b2.shape[0]))
    difference = cv2.absdiff(b1, b2)
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    total_diff = np.sum(gray_difference)
    threshold = 30
    if total_diff > threshold:
        return True
    return False


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

    def refresh_board(self):
        board = screenshot_region(self.x, self.y,
                                  self.w, self.h)
        self.current_board = normalize(board)

    def move(self, move):
        from_square, to_square = parse_move(move)
        x, y = self.get_coord_from_square(from_square)
        pyautogui.click(x + self.x, y + self.y)
        x, y = self.get_coord_from_square(to_square)
        pyautogui.click(x + self.x, y + self.y)
        pyautogui.moveTo(1, 1)

    def wait_move(self):
        diff = False
        while diff is False:
            board = normalize(screenshot_region(self.x, self.y,
                                                self.w, self.h))
            diff = diff_board(self.current_board, board)
            time.sleep(0.1)


def get_board_coord(img_fullscreen):
    """
    Get the coordinates of a board from a full screenshot.
    """
    target_color = np.array(WHITE_SQUARE_COLOR)
    # Define a small tolerance range around the target color
    tolerance = np.array([2, 2, 2])
    # Create the minimum and maximum color ranges
    lower_color = target_color - tolerance
    upper_color = target_color + tolerance
    # Ensure that the color values remain within the [0, 255] range
    lower_color = np.clip(lower_color, 0, 255)
    upper_color = np.clip(upper_color, 0, 255)
    # Create a mask for the target color
    mask = cv2.inRange(img_fullscreen, lower_color, upper_color)
    # Find the coordinates of the first non-zero pixel
    coords = cv2.findNonZero(mask)
    assert coords is not None
    x1, y1 = coords[0][0]
    x2, y2 = coords[-1][-1]
    return int(x1 - 1), int(y1 - 1), int(x2 + 1), int(y2 + 1)
