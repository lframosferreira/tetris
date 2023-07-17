import pygame
from abc import ABC, abstractmethod
import sys

sys.path.append("..")

from constants import *


class Piece(ABC):
    def __init__(self, color: tuple[int, int, int]) -> None:
        self.color: tuple[int, int, int] = color
        # self.body = [] como definir isso
        self.collided: bool = False

    def draw(self, screen) -> None:
        for block in self.body:
            block.draw(screen=screen)

    def drop(self) -> None:
        for block in self.body:
            block.body.y += BLOCK_SIZE

    def move(self, direction: int) -> None:
        for block in self.body:
            block.body.x += direction * BLOCK_SIZE

    def is_on_left_edge(self, board: pygame.Rect) -> bool:
        return any([block.is_on_left_edge(board=board) for block in self.body])

    def is_on_right_edge(self, board: pygame.Rect) -> bool:
        return any([block.is_on_right_edge(board=board) for block in self.body])

    def collided_with(self, other) -> bool:
        return any([block.collided_with_list(other.body) for block in self.body])

    """
        checks if piece collided with floor or any of the other pieces on screen
    """

    def collided_with_obstacle(self, pieces_on_screen: list) -> bool:
        collided_with_floor: bool = any(
            [
                block.body.y == BOARD_TOP + BOARD_HEIGHT - BLOCK_SIZE
                for block in self.body
            ]
        )
        collided_with_pieces_on_screen: bool = any(
            [
                self.collided_with(piece_on_screen)
                for piece_on_screen in pieces_on_screen
            ]
        )
        self.collided = collided_with_floor or collided_with_pieces_on_screen
        return collided_with_floor or collided_with_pieces_on_screen

    @abstractmethod
    def rotate(self) -> None:
        pass
