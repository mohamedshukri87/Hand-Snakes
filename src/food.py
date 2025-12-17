import random, pygame

class Food:
    def __init__(self, board, colour, step):

        self.board = board
        self.colour = colour
        self._step = step
        self.coordinates = [-1, -1]
    
    def getStep(self):
        return self._step
    
    def setCoordinates(self, arr):
        self.coordinates = arr
    
    def getCoordinates(self):
        return self.coordinates
    
    def validCoordinates(self):


        return self.getCoordinates() != [-1, -1]
  
    def generateRandomCoordinates(self, x, y):
        return [ random.randrange(0, x, 30), random.randrange(0, y, 30) ]

    def spawnFood(self, x, y):
        randomCoordinates = self.generateRandomCoordinates(x, y)

        self.setCoordinates(randomCoordinates)
        return randomCoordinates

        