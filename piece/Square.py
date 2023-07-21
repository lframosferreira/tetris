import pygame
import sys

sys.path.append("..")

from constants import *

from .Piece import Piece, is_inside_board


class Square(Piece):
    def __init__(self, color: tuple[int, int, int]) -> None:
        super().__init__(color=color)
        self.body: list[pygame.Rect] = [
            pygame.Rect(4 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(5 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(
                4 * BLOCK_SIZE + BOARD_LEFT,
                BLOCK_SIZE + BOARD_TOP,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
            pygame.Rect(
                5 * BLOCK_SIZE + BOARD_LEFT,
                BLOCK_SIZE + BOARD_TOP,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
        ]

    def rotate(
        self, pieces_on_screen: list, board: pygame.Rect, direction: int
    ) -> None:
        pass
