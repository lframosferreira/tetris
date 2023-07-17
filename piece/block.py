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

    def is_on_left_edge(self, board: pygame.Rect) -> bool:
        return self.body.x == BOARD_LEFT

    def is_on_right_edge(self, board: pygame.Rect) -> bool:
        return self.body.x == BOARD_LEFT + BOARD_WIDTH - BLOCK_SIZE

    def collided_with(self, other) -> bool:
        return self.body.colliderect(other)

    def collided_with_list(self, others_list) -> bool:
        return self.body.collidelist([other.body for other in others_list])
