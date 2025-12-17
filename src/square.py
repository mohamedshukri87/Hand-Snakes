import pygame
import random
class Square:
    def __init__(self, x, y, screen, numSquare):
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.numSquare = numSquare


    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getScreen(self):
        return self.__screen
    
    def getColour(self):

        return (144,238,144) if self.numSquare%2==0 else (0, 100, 0)
    
    def getRect(self):
        return pygame.Rect(self.getX(),self.getY(),50,50)
   
    
    def drawSquare(self): 
        pygame.draw.rect(self.getScreen(), self.getColour(), self.getRect())

    