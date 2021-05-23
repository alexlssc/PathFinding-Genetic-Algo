import pygame
import sys
from indiv import Individual as indi

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
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Path-Finding Genetic Algorithm")
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    # Init population
    pop = [indi(400, 100, GENE_LENGTH, ENTITY_COLOUR, SCREEN)
           for _ in range(NB_POP)]
    for indiv in pop:
        indiv.setRandomGenes()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for gen in range(NB_GEN):
            allFitness = []
            for _ in range(GENE_LENGTH):
                SCREEN.fill(BACKGROUND)
                CLOCK.tick(FPS)
                text_surface = font.render(
                    f'Generation: {gen}', True, (255, 255, 255))
                SCREEN.blit(text_surface, dest=(0, 0))
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
