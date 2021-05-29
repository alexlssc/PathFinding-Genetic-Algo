import random
import pygame
import sys
import math
from indiv import Individual as indi

SIZE = width, height = 800, 800
BACKGROUND = [8, 126, 139]
ENTITY_COLOUR = [255, 90, 95]
FPS = 40
ENDPOINT = x, y = 400, 700
NB_POP = 100
NB_GEN = 50
MUTATION_RATE = 0.02

GENE_LENGTH = 250


def printText(text, font, location=(0, 0)):
    """Print text onto the screen

    Args:
        text (String): Text displayed on screen
        font (pygame.Font): Font used to display text
        location (tuple, optional): x, y coordinates for text position. Defaults to (0, 0).
    """
    text_surface = font.render(
        text, True, (255, 255, 255))
    SCREEN.blit(text_surface, dest=location)
    pygame.draw.circle(SCREEN, ENTITY_COLOUR, ENDPOINT, 20)


def proceedNaturalSelection(pop, best_fitness, best_overall_fitness):
    """Create and return mating pool using just finished current generation.
       Also working out best fitness value and overall best fitness value

    Args:
        pop ([Individual]): Population from the current generationddfjkf
        best_fitness (Float): Best fitness value since the beginning of the simulatiom
        best_overall_fitness (Float): Best overall fitness since the beginning of the simulation

    Returns:
        matingPool ([[pygame.Vector2]]) : Completed mating pool
        best_fitness (Float) : Newly worked-out Best Fitness
        best_overall_fitness (Float) : Newly worked-out Best Overall Fitness
    """
    matingPool = []
    this_overall_fitness = 0
    for indiv in pop:
        n = math.floor(indiv.getFitness() * 100)
        this_overall_fitness += n
        if n > best_fitness:
            best_fitness = n
        for _ in range(n):
            matingPool.append(indiv.getGenes())

    if this_overall_fitness / len(pop) > best_overall_fitness:
        best_overall_fitness = this_overall_fitness / len(pop)
    return matingPool, best_fitness, best_overall_fitness


def reproduce(matingPool):
    """ Return the next generation of population 

    Args:
        matingPool ([[pygame.Vector2]]) : Current generation matingPool

    Returns:
        nextGen ([Individual]) : List of individual for the next generation
    """
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
    """Create and return Child Individual object according to the mum and fathers' DNA

    Args:
        mum ([[pygame.Vector2]]): Mother's DNA picked from the mating pool
        dad ([[pygame.Vector2]]): Father's DNA picked from the mating pool

    Returns:
        child (Individual) : Individual object created from mother and father's DNA
    """
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
    """Introduce random mutation into the child's DNA

    Args:
        dna ([[pygame.Vector2]]): Child's DNA without mutation

    Returns:
        dna ([[pygame.Vector2]]): Child's DNA with potential mutation
    """
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
    best_overall_fitness = 0
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
                printText(
                    f'Best Overall Fitness: {best_overall_fitness}', font, location=(0, 40))
                for indiv in pop:
                    indiv.draw()
                CLOCK.tick(FPS)
                pygame.display.flip()

            matingPool, best_fitness, best_overall_fitness = proceedNaturalSelection(
                pop, best_fitness, best_overall_fitness)
            pop = reproduce(matingPool)

        break


if __name__ == "__main__":
    main()
