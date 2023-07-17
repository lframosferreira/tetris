import pygame
import sys

sys.path.append("..")

from constants import *

from .block import Block
from .piece import Piece


class Square(Piece):
    def __init__(self, color: tuple[int, int, int]) -> None:
        super().__init__(color=color)
        self.body: list[Block] = [
            Block(left=7 * BLOCK_SIZE + BOARD_LEFT, top=BOARD_TOP, color=self.color),
            Block(left=8 * BLOCK_SIZE + BOARD_LEFT, top=BOARD_TOP, color=self.color),
            Block(
                left=7 * BLOCK_SIZE + BOARD_LEFT,
                top=BLOCK_SIZE + BOARD_TOP,
                color=self.color,
            ),
            Block(
                left=8 * BLOCK_SIZE + BOARD_LEFT,
                top=BLOCK_SIZE + BOARD_TOP,
                color=self.color,
            ),
        ]

    def rotate(self, screen) -> None:
        pass
