import pygame
import sys

sys.path.append("..")

from constants import *

from .piece import Piece


class Square(Piece):
    def __init__(self, color: tuple[int, int, int]) -> None:
        super().__init__(color=color)
        self.body: list[pygame.Rect] = [
            pygame.Rect(7 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(8 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(
                7 * BLOCK_SIZE + BOARD_LEFT,
                BLOCK_SIZE + BOARD_TOP,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
            pygame.Rect(
                8 * BLOCK_SIZE + BOARD_LEFT,
                BLOCK_SIZE + BOARD_TOP,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
        ]

    def rotate(self) -> None:
        pass
