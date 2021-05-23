import pygame
import sys
from indiv import Individual as indi

pygame.init()
pygame.display.set_caption("Path-Finding Genetic Algorithm")

SIZE = width, height = 800, 800
BACKGROUND = [8, 126, 139]
ENTITY_COLOUR = [255, 90, 95]
FPS = 10
ENDPOINT = x, y = 400, 700
NB_POP = 50
NB_GEN = 1

GENE_LENGTH = 80


def main():
    global SCREEN
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()

    # Init population
    pop = [indi(400, 100, GENE_LENGTH, ENTITY_COLOUR, SCREEN)
           for _ in range(NB_POP)]
    for indiv in pop:
        indiv.setRandomGenes()

    allFitness = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for _ in range(NB_GEN):
            for _ in range(GENE_LENGTH):
                SCREEN.fill(BACKGROUND)
                CLOCK.tick(FPS)
                pygame.draw.circle(SCREEN, ENTITY_COLOUR, ENDPOINT, 20)
                for indiv in pop:
                    indiv.draw()
                pygame.display.flip()
        else:
            for indiv in pop:
                allFitness.append(indiv.getFitness())
            print(allFitness)
        break


if __name__ == "__main__":
    main()
