import pygame
import sys
import copy

sys.path.append("..")

from constants import *

from .Piece import Piece


class T(Piece):
    def __init__(self, color: tuple[int, int, int]) -> None:
        super().__init__(color=color)
        self.body: list[pygame.Rect] = [
            pygame.Rect(3 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(4 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(5 * BLOCK_SIZE + BOARD_LEFT, BOARD_TOP, BLOCK_SIZE, BLOCK_SIZE),
            pygame.Rect(
                4 * BLOCK_SIZE + BOARD_LEFT,
                BOARD_TOP + BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            ),
        ]

    def rotate(self, pieces_on_screen: list, direction: int) -> None:
        future_body: list = copy.deepcopy(self.body)
        if self.state == 0 or self.state == 2:
            future_body[3].x += BLOCK_SIZE * (1 if self.state == 0 else -1)
            future_body[3].y += BLOCK_SIZE * (1 if self.state == 0 else -1)
            for i, block in enumerate(future_body[:-1]):
                block.x += BLOCK_SIZE * (1 - i) * (1 if self.state == 0 else -1)
                block.y += BLOCK_SIZE * (1 - i) * (-1 if self.state == 0 else 1)
        elif self.state == 1 or self.state == 3:
            future_body[3].x += BLOCK_SIZE * (-1 if self.state == 1 else 1)
            future_body[3].y += BLOCK_SIZE * (1 if self.state == 1 else -1)
            for i, block in enumerate(future_body[:-1]):
                block.x += BLOCK_SIZE * (1 - i) * (1 if self.state == 1 else -1)
                block.y += BLOCK_SIZE * (1 - i) * (1 if self.state == 1 else -1)
            pass
        else:
            print("Something went wrong with the piece state")
        can_move: bool = True
        for future_block in future_body:
            can_move = can_move and all(
                [
                    future_block.collidelist(piece_on_screen.body) == -1
                    for piece_on_screen in pieces_on_screen
                ]
            )
        if can_move:
            self.body = future_body
            self.state = int((self.state + 1) % 4)

