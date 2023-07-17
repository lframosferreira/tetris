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

    def draw(self, screen) -> None:
        for block in self.body:
            block.draw(screen=screen)

    def rotate(self, screen) -> None:
        pass

    def drop(self) -> None:
        for block in self.body:
            block.body.y += BLOCK_SIZE

    def move(self, direction: int) -> None:
        for block in self.body:
            block.body.x += direction * BLOCK_SIZE

    def is_inside_board(self, board: pygame.Rect) -> bool:
        gambiarra_board = pygame.Rect(
            board.x + BLOCK_SIZE, board.y, BOARD_WIDTH - BLOCK_SIZE, BOARD_HEIGHT
        )
        return all([board.contains(block.body) for block in self.body])
