import pygame

pygame.init()

from constants import *

from piece import Block, Square

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")


def draw_board(
    board_upper_left_pos: tuple[int, int], board_width: int, board_height: int
) -> None:
    rect = pygame.Rect(*board_upper_left_pos, BOARD_WIDTH, BOARD_HEIGHT)
    pygame.draw.rect(SCREEN, GREY, rect, width=1)

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
    pieces_on_screen: list = [Square(color=RED)]
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        draw_board(
            board_upper_left_pos=BOARD_UPPER_LEFT_POS,
            board_width=BOARD_WIDTH,
            board_height=BOARD_HEIGHT,
        )
        for piece in pieces_on_screen:
            piece.draw(screen=SCREEN)
    pygame.quit()


if __name__ == "__main__":
    main()
