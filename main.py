import random
import pygame
import sys
import math
from indiv import Individual as indi

SIZE = width, height = 800, 800
BACKGROUND = [8, 126, 139]
ENTITY_COLOUR = [255, 90, 95]
FPS = 10
ENDPOINT = x, y = 400, 700
NB_POP = 50
NB_GEN = 30
MUTATION_RATE = 0.02

GENE_LENGTH = 80


def printText(text, font, location=(0, 0)):
    text_surface = font.render(
        text, True, (255, 255, 255))
    SCREEN.blit(text_surface, dest=location)
    pygame.draw.circle(SCREEN, ENTITY_COLOUR, ENDPOINT, 20)


def proceedNaturalSelection(pop, best_fitness):
    matingPool = []
    for indiv in pop:
        n = math.floor(indiv.getFitness() * 100)
        if n > best_fitness:
            best_fitness = n
        for _ in range(n):
            matingPool.append(indiv.getGenes())
    return matingPool, best_fitness


def reproduce(matingPool):
    nextGen = []
    for _ in range(NB_POP):
        mumIndex = random.randrange(len(matingPool))
        dadIndex = random.randrange(len(matingPool))

        mum = matingPool[mumIndex]
        dad = matingPool[dadIndex]

        child = getChild(mum, dad)
        nextGen.append(child)

    return nextGen


def getChild(mum, dad):
    childDna = []
    for i in range(len(mum)):
        if i % 2 == 0:
            childDna.append(mum[i])
        else:
            childDna.append(dad[i])

    childDna = getMutation(childDna)
    child = indi(400, 100, GENE_LENGTH, ENTITY_COLOUR, SCREEN, childDna)
    return child


def getMutation(dna):
    for idx, _ in enumerate(dna):
        if random.random() < MUTATION_RATE:
            dna[idx] = pygame.Vector2(
                random.random()-0.5, random.random()-0.5)
    return dna


def main():
    global SCREEN
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Path-Finding Genetic Algorithm")
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()
    best_fitness = 0
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
            for _ in range(GENE_LENGTH):
                SCREEN.fill(BACKGROUND)
                printText(f'Generation: {gen+1}', font, location=(0, 0))
                printText(
                    f'Best Fitness: {best_fitness}', font, location=(0, 20))
                for indiv in pop:
                    indiv.draw()
                CLOCK.tick(FPS)
                pygame.display.flip()

            matingPool, best_fitness = proceedNaturalSelection(
                pop, best_fitness)
            pop = reproduce(matingPool)

        break


if __name__ == "__main__":
    main()
