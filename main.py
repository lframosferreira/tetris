import pygame

pygame.init()

from constants import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")


def main():
    run: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()
