import pygame
import sys

sys.path.append("..")

from constants import *


class Block:
    def __init__(
        self, left: int, top: int, color: tuple[int, int, int] = WHITE
    ) -> None:
        self.color = color
        self.body: pygame.Rect = pygame.Rect(left, top, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen) -> None:
        pygame.draw.rect(surface=screen, rect=self.body, color=self.color)
