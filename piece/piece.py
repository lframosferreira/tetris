import pygame
from abc import ABC, abstractmethod
import sys

sys.path.append("..")

from constants import *


class Piece(ABC):
    def __init__(self, color: tuple[int, int, int]) -> None:
        self.color: tuple[int, int, int] = color
        # self.body: list[pygame.Rect] = [] como definir isso
        self.collided: bool = False

    def draw(self, screen) -> None:
        for block in self.body:
            pygame.draw.rect(surface=screen, rect=block, color=self.color)

    def drop(self) -> None:
        for block in self.body:
            block.y += BLOCK_SIZE

    def move(self, direction: int) -> None:
        for block in self.body:
            block.x += direction * BLOCK_SIZE

    def is_on_left_edge(self) -> bool:
        return any([block.x == BOARD_LEFT for block in self.body])

    def is_on_right_edge(self) -> bool:
        return any(
            [block.x == BOARD_LEFT + BOARD_WIDTH - BLOCK_SIZE for block in self.body]
        )

    def will_collide_with(self, other) -> bool:
        future_body: list[pygame.Rect] = self.body.copy()
        for block in future_body:
            block.y += BLOCK_SIZE
        return any([block.collidelist(other.body) != -1 for block in future_body])

    """
        checks if piece collided with floor or any of the other pieces on screen
    """

    def will_collide_with_obstacle(self, pieces_on_screen: list) -> bool:
        collided_with_floor: bool = any(
            [block.y == BOARD_TOP + BOARD_HEIGHT - BLOCK_SIZE for block in self.body]
        )
        collided_with_pieces_on_screen: bool = any(
            [
                self.will_collide_with(other=piece_on_screen)
                for piece_on_screen in pieces_on_screen
            ]
        )
        self.collided = collided_with_floor or collided_with_pieces_on_screen
        return collided_with_floor or collided_with_pieces_on_screen

    @abstractmethod
    def rotate(self) -> None:
        pass
