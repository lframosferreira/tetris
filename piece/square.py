import pygame
import sys

sys.path.append("..")

from constants import *

from .block import Block


class Square:
    def __init__(self, color: tuple[int, int, int]) -> None:
        self.color: tuple[int, int, int] = color
        self.body: list[Block] = [
            Block(left=7 * BLOCK_SIZE, top=0, color=self.color),
            Block(left=8 * BLOCK_SIZE, top=0, color=self.color),
            Block(left=7 * BLOCK_SIZE, top=BLOCK_SIZE, color=self.color),
            Block(left=8 * BLOCK_SIZE, top=BLOCK_SIZE, color=self.color),
        ]

    def draw(self, screen) -> None:
        for block in self.body:
            block.draw(screen=screen)
