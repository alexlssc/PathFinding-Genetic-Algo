import random
import pygame
import math


class Individual:
    def __init__(self, x, y, GENES_LENGTH, ENTITY_COLOUR, SCREEN, genes=[]) -> None:
        self.x = x
        self.y = y
        self.size = 5
        self.GENES_LENGTH = GENES_LENGTH
        self.ENTITY_COLOUR = ENTITY_COLOUR
        self.SCREEN = SCREEN
        self.genes = genes
        self.index = 0
        self.velocity = 25
        self.done = False
        self.fitness = 0

    def update(self):
        """Update Individuals value per frame
        """
        try:
            self.x += self.velocity*self.genes[self.index].x
            self.y += self.velocity*self.genes[self.index].y
            self.setFitness((400, 700))
        except:
            self.done = True
        self.index += 1
        self.done = self.checkOutOfBounds()

    def checkOutOfBounds(self):
        """Check if individual is within the screen's bounds

        Returns:
            Boolean : Boolean whether the individual is within the screen's bounds or not
        """
        if self.x < 0 or self.x > self.SCREEN.get_width() or self.y < 0 or self.y > self.SCREEN.get_height():
            return True

        return False

    def draw(self):
        """Draw Individual on the screen if Individual not done
        """
        if self.done == False:
            self.update()
            pygame.draw.rect(self.SCREEN, self.ENTITY_COLOUR,
                             pygame.Rect(self.x, self.y, self.size, self.size))

    def calcFitness(self, endpoint):
        """Workouts Individual's fitness score (Distance to EndPoint)

        Args:
            endpoint (float, float): x,y coordinates of the endpoint

        Returns:
            fitness_score (float): Fitness score of this individual
        """
        distanceToEndpoint = self.calcDistance(endpoint)
        normalised = distanceToEndpoint / self.SCREEN.get_height()
        return 1 - normalised

    def setFitness(self, endpoint):
        self.fitness = self.calcFitness(endpoint)

    def getFitness(self):
        return self.fitness

    def calcDistance(self, endpoint):
        """Works out distance between 2 points

        Args:
            endpoint (float, float): x,y coordinates of the endpoint

        Returns:
            distance (float): Distance between individual and endpoint
        """
        endpoint_x, endpoint_y = endpoint
        return math.sqrt((self.x-endpoint_x)**2 + (self.y-endpoint_y)**2)

    def setGenes(self, genes):
        self.genes = genes

    def setRandomGenes(self):
        self.genes = [pygame.Vector2(
            random.random()-0.5, random.random()-0.5) for _ in range(self.GENES_LENGTH)]

    def getGenes(self):
        return self.genes

    def getDone(self):
        return self.done
