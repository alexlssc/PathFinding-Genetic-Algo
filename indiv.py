import random
import pygame
from pygame.sndarray import array


class Individual:
    def __init__(self, x, y, GENES_LENGTH, ENTITY_COLOUR, SCREEN) -> None:
        self.x = x
        self.y = y
        self.size = 5
        self.GENES_LENGTH = GENES_LENGTH
        self.ENTITY_COLOUR = ENTITY_COLOUR
        self.SCREEN = SCREEN
        self.genes = []
        self.index = 0
        self.velocity = 25

    def update(self):
        self.x += self.velocity*self.genes[self.index].x
        self.y += self.velocity*self.genes[self.index].y
        self.index += 1

    def draw(self):
        self.update()
        pygame.draw.rect(self.SCREEN, self.ENTITY_COLOUR,
                         pygame.Rect(self.x, self.y, self.size, self.size))

    def setGenes(self, genes):
        self.genes = genes

    def setRandomGenes(self):
        self.genes = [pygame.Vector2(
            random.random()-0.5, random.random()-0.5) for _ in range(self.GENES_LENGTH)]

    def getGenes(self):
        return self.genes
