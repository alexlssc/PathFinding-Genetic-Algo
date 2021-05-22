import pygame
import sys

pygame.init()
pygame.display.set_caption("Path-Finding Genetic Algorithm")

SIZE = width, height = 800, 800
BACKGROUND = [8, 126, 139]
FPS = 30


def main():
    global SCREEN
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        CLOCK.tick(FPS)
        SCREEN.fill(BACKGROUND)
        pygame.display.flip()


if __name__ == "__main__":
    main()
