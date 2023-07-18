import pygame

pygame.init()

import random
from constants import *

from piece import Square

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# events
PIECE_DROP_DELAY: int = 250
PIECE_DROP_EVENT: int = pygame.USEREVENT + 1
pygame.time.set_timer(event=PIECE_DROP_EVENT, millis=PIECE_DROP_DELAY)


def draw_board(board: pygame.Rect) -> None:
    pygame.draw.rect(SCREEN, GREY, board, width=1)
    board_upper_left_pos: tuple[int, int] = board.x, board.y

    # grid for helping debugging
    for i in range(BOARD_WIDTH // BLOCK_SIZE):
        pygame.draw.line(
            SCREEN,
            GREY,
            (board_upper_left_pos[0] + BLOCK_SIZE * i, board_upper_left_pos[1]),
            (
                board_upper_left_pos[0] + BLOCK_SIZE * i,
                board_upper_left_pos[1] + BOARD_HEIGHT,
            ),
        )
    for i in range(BOARD_HEIGHT // BLOCK_SIZE):
        pygame.draw.line(
            SCREEN,
            GREY,
            (board_upper_left_pos[0], board_upper_left_pos[1] + BLOCK_SIZE * i),
            (
                board_upper_left_pos[0] + BOARD_WIDTH,
                board_upper_left_pos[1] + BLOCK_SIZE * i,
            ),
        )


def main():
    run: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()
    BOARD: pygame.Rect = pygame.Rect(*BOARD_UPPER_LEFT_POS, BOARD_WIDTH, BOARD_HEIGHT)
    pieces_on_screen: list = [Square(color=RED)]
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
                    pieces_on_screen[-1].move(direction=-1)
                elif (
                    event.key == pygame.K_RIGHT
                    and not pieces_on_screen[-1].is_on_right_edge()
                ):
                    pieces_on_screen[-1].move(direction=1)
                elif (event.key == pygame.K_UP):
                    pieces_on_screen[-1].rotate()
            elif event.type == PIECE_DROP_EVENT:
                pieces_on_screen[-1].drop()
        if pieces_on_screen[-1].will_collide_with_obstacle(
            pieces_on_screen=pieces_on_screen[:-1]
        ):
            pieces_on_screen.append(Square(color=GREEN))
        SCREEN.fill(BLACK)
        draw_board(board=BOARD)
        for piece in pieces_on_screen:
            piece.draw(screen=SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
