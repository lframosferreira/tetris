import pygame
from abc import ABC, abstractmethod
import sys
import copy

sys.path.append("..")

from constants import *


def is_inside_board(block: pygame.Rect, board: pygame.Rect) -> bool:
    return board.contains(block)


class Piece(ABC):
    def __init__(self, color: tuple[int, int, int]) -> None:
        self.color: tuple[int, int, int] = color
        self.body: list[pygame.Rect] = []
        self.collided: bool = False
        self.state: int = 0

    def draw(self, screen) -> None:
        for block in self.body:
            pygame.draw.rect(surface=screen, rect=block, color=self.color)
        for block in self.body:
            pygame.draw.rect(surface=screen, rect=block, color=BLACK, width=2)

    def drop(self) -> None:
        for block in self.body:
            block.y += BLOCK_SIZE

    def move(self, direction: int, pieces_on_screen: list) -> None:
        future_body: list[pygame.Rect] = copy.deepcopy(self.body)
        for block in future_body:
            block.x += direction * BLOCK_SIZE
        can_move: bool = True
        for future_block in future_body:
            can_move = can_move and all(
                [
                    future_block.collidelist(piece_on_screen.body) == -1
                    for piece_on_screen in pieces_on_screen
                ]
            )
        if can_move:
            for block in self.body:
                block.x += direction * BLOCK_SIZE

    def is_on_left_edge(self) -> bool:
        return any([block.x == BOARD_LEFT for block in self.body])

    def is_on_right_edge(self) -> bool:
        return any(
            [block.x == BOARD_LEFT + BOARD_WIDTH - BLOCK_SIZE for block in self.body]
        )

    def will_collide_with(self, other) -> bool:
        future_body: list[pygame.Rect] = copy.deepcopy(self.body)
        for block in future_body:
            block.y += BLOCK_SIZE
        return any([block.collidelist(other.body) != -1 for block in future_body])

    def is_colliding_with_obstacle(self, pieces_on_screen: list) -> bool:

        collided_with_pieces_on_screen: bool = any(
            [
                any([block.collidelist(piece_on_screen.body) != -1 for block in self.body])
                for piece_on_screen in pieces_on_screen
            ]
        )
        return collided_with_pieces_on_screen

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
    def rotate(
        self, pieces_on_screen: list, board: pygame.Rect, direction: int
    ) -> None:
        pass
