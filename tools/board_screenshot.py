#!/usr/bin/env python3

import cv2
import sys

from argparse import ArgumentParser

from interface import get_board_coord
from utils import screenshot_full, screenshot_region


def main(argv: list[str]):
    parser = ArgumentParser()
    parser.add_argument("--img", required=True)
    parser.add_argument("--extract-board", action="store_true")
    opts = parser.parse_args(argv)
    img = screenshot_full()
    if opts.extract_board:
        x1, y1, x2, y2 = get_board_coord(img)
        img = screenshot_region(x1, y1, x2 - x1, y2 - y1)
    cv2.imwrite(opts.img, img)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
