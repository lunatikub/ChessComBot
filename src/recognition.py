"""
Allows recognizing the pieces on an image of a chessboard.
"""

import cv2
import numpy as np

from board import Board, FILES_MAP, RANKS_MAP
from pieces import PIECES


# BGR square colors on chess.com
WHITE_SQUARE_COLOR = [208, 236, 235]
BLACK_SQUARE_COLOR = [82, 149, 115]
YELLOW1_SQUARE_COLOR = [67, 202, 185]
YELLOW2_SQUARE_COLOR = [130, 246, 245]


def normalize(board):
    """
    Normalize a chessboard image to facilitate piece recognition.
    """
    board = mask_color(board, BLACK_SQUARE_COLOR, WHITE_SQUARE_COLOR)
    board = mask_color(board, YELLOW1_SQUARE_COLOR, WHITE_SQUARE_COLOR)
    board = mask_color(board, YELLOW2_SQUARE_COLOR, WHITE_SQUARE_COLOR)
    return board


def mask_color(img, color_src, color_dst):
    """
    Apply a mask to replace color_src by color_dst.
    """
    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Color to update.
    bgr_color_to_change = np.uint8([[color_src]])
    hsv_color_to_change = cv2.cvtColor(bgr_color_to_change, cv2.COLOR_BGR2HSV)
    # Obtain the thresholds
    hue = hsv_color_to_change[0][0][0]
    saturation = hsv_color_to_change[0][0][1]
    value = hsv_color_to_change[0][0][2]
    # Set a tolerance range for color detection.
    tolerance = 30
    lower_color = np.array([
        hue - tolerance,
        max(int(saturation) - tolerance, 0),
        max(int(value) - tolerance, 0)])
    upper_color = np.array([
        hue + tolerance,
        min(int(saturation) + tolerance, 255),
        min(int(value) + tolerance, 255)])
    # Create a mask that captures the areas of the image within the color range
    mask = cv2.inRange(hsv, lower_color, upper_color)
    # New color to apply.
    new_bgr_color = color_dst
    # Update the color when the mask is true.
    img[mask > 0] = new_bgr_color
    return img


def recognize_piece(interface, board, img_board, piece):
    threshold = 0.8
    result = cv2.matchTemplate(img_board, piece.template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    w, h = piece.template.shape[::-1]
    squares = []
    for loc in locations:
        x = (loc[0] + loc[0] + w) / 2
        y = (loc[1] + loc[1] + h) / 2
        squares.append(interface.get_square_from_coord(x, y))
    for s in set(squares):
        f = FILES_MAP[s[0]]
        r = RANKS_MAP[s[1]]
        board.b[r][f] = piece


def recognize(interface, img_board):
    """
    Return a board with all pieces recognized from an image of the board.
    """
    img_board = cv2.cvtColor(img_board, cv2.COLOR_BGR2GRAY)
    board = Board()
    for p in PIECES:
        recognize_piece(interface, board, img_board, p)
    return board
