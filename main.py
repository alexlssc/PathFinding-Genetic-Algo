import pygame
import sys
import pandas
from indiv import Individual as indi

pygame.init()
pygame.display.set_caption("Path-Finding Genetic Algorithm")

SIZE = width, height = 800, 800
BACKGROUND = [8, 126, 139]
ENTITY_COLOUR = [255, 90, 95]
FPS = 10
ENDPOINT = x, y = 400, 700
NB_POP = 50

GENE_LENGTH = 50


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

        CLOCK.tick(FPS)
        SCREEN.fill(BACKGROUND)

        for indiv in pop:
            indiv.draw()

        pygame.draw.circle(SCREEN, ENTITY_COLOUR, ENDPOINT, 20)
        for indiv in pop:
            indiv.setFitness(ENDPOINT)
            print(indiv.getFitness())
        pygame.display.flip()


def createGenes():
    return [pygame.Vector2 for _ in range(GENE_LENGTH)]


if __name__ == "__main__":
    main()
