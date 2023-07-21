import pygame

pygame.init()
import time

import random
import itertools
from constants import *

from piece import Square, I, LeftGun, RightGun, LeftSnake, RightSnake, T

PIECES: list = [Square, I, LeftGun, RightGun, LeftSnake, RightSnake, T]
COLORS: list = [RED, GREEN, BLUE, GREY]

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# events
PIECE_DROP_DELAY: int = 200
PIECE_DROP_EVENT: int = pygame.USEREVENT + 1
pygame.time.set_timer(event=PIECE_DROP_EVENT, millis=PIECE_DROP_DELAY)


def draw_board(board: pygame.Rect) -> None:
    pygame.draw.rect(SCREEN, BLACK, board, width=2)
    board_upper_left_pos: tuple[int, int] = board.x, board.y

    # grid for helping debugging
    for i in range(BOARD_WIDTH // BLOCK_SIZE):
        pygame.draw.line(
            SCREEN,
            BLACK,
            (board_upper_left_pos[0] + BLOCK_SIZE * i, board_upper_left_pos[1]),
            (
                board_upper_left_pos[0] + BLOCK_SIZE * i,
                board_upper_left_pos[1] + BOARD_HEIGHT,
            ),
            2,
        )
    for i in range(BOARD_HEIGHT // BLOCK_SIZE):
        pygame.draw.line(
            SCREEN,
            BLACK,
            (board_upper_left_pos[0], board_upper_left_pos[1] + BLOCK_SIZE * i),
            (
                board_upper_left_pos[0] + BOARD_WIDTH,
                board_upper_left_pos[1] + BLOCK_SIZE * i,
            ),
            2,
        )


def check_line_clean(board: pygame.Rect, pieces_on_screen: list) -> None:
    blocks_in_screen: list = [
        (piece_on_screen, piece_on_screen.body) for piece_on_screen in pieces_on_screen
    ]
    blocks_in_screen = [
        (piece_on_screen, block)
        for (piece_on_screen, body) in blocks_in_screen
        for block in body
    ]

    for row in range(
        BOARD_UPPER_LEFT_POS[1] + board.height - BLOCK_SIZE,
        BOARD_UPPER_LEFT_POS[1] - BLOCK_SIZE,
        -BLOCK_SIZE,
    ):
        can_remove: bool = True
        collision_indexes: list[int] = []
        for col in range(
            BOARD_UPPER_LEFT_POS[0], BOARD_UPPER_LEFT_POS[0] + board.width, BLOCK_SIZE
        ):
            aux_rect: pygame.Rect = pygame.Rect(col, row, BLOCK_SIZE, BLOCK_SIZE)
            collision_index: int = aux_rect.collidelist(
                [b[1] for b in blocks_in_screen]
            )
            if collision_index == -1:
                can_remove = False
            else:
                collision_indexes.append(collision_index)
        if can_remove:
            for index in collision_indexes:
                blocks_in_screen[index][0].body.remove(blocks_in_screen[index][1])
            for _, block in blocks_in_screen:
                if block.y < row:
                    block.y += BLOCK_SIZE


def main():
    run: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()
    BOARD: pygame.Rect = pygame.Rect(*BOARD_UPPER_LEFT_POS, BOARD_WIDTH, BOARD_HEIGHT)
    pieces_on_screen: list = [T(color=GREEN)]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_LEFT
                    and not pieces_on_screen[-1].is_on_left_edge()
                ):
                    pieces_on_screen[-1].move(
                        direction=-1, pieces_on_screen=pieces_on_screen[:-1]
                    )
                elif (
                    event.key == pygame.K_RIGHT
                    and not pieces_on_screen[-1].is_on_right_edge()
                ):
                    pieces_on_screen[-1].move(
                        direction=1, pieces_on_screen=pieces_on_screen[:-1]
                    )
                elif event.key == pygame.K_z:
                    pieces_on_screen[-1].rotate(
                        pieces_on_screen=pieces_on_screen[:-1],
                        board=BOARD,
                        direction=-1,
                    )
                elif event.key == pygame.K_x:
                    pieces_on_screen[-1].rotate(
                        pieces_on_screen=pieces_on_screen[:-1], board=BOARD, direction=1
                    )
            elif event.type == PIECE_DROP_EVENT:
                pieces_on_screen[-1].drop()
        if pieces_on_screen[-1].will_collide_with_obstacle(
            pieces_on_screen=pieces_on_screen[:-1]
        ):
            random_piece = random.choice(PIECES)
            random_color = random.choice(COLORS)
            pieces_on_screen.append(random_piece(color=random_color))
        check_line_clean(board=BOARD, pieces_on_screen=pieces_on_screen[:-1])
        SCREEN.fill(WHITE)
        draw_board(board=BOARD)
        for piece in pieces_on_screen:
            piece.draw(screen=SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
