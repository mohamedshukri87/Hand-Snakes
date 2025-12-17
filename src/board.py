

from square import Square
from food import Food
from snakeObject import Snake

from lib import checks
import random
import pygame

class Board:
    def __init__(self, row, col, screen):

        self.__row = row # row, col = not neccessary now
        self.__col = col
        self.screen = screen
        self.squareArrays = []
        self.snake = Snake(90, 240) # the snake object is free for anybody to see.
        self.food = Food(self, (255,0,0), 30)
        
    
    def getRow(self):
        return self.__row
    def getCol(self):
        return self.__col
    def getScreen(self):
        return self.screen
    def appendToSquareArrays(self, square):
        self.squareArrays.append(square)
    
    def getSquareArrays(self):
        return self.squareArrays
    def validSnakeHead(self):
        boolean = True if len(self.snake.getCoordinates()) < 2 else self.snake.getHead() not in self.snake.getCoordinates()[1:]

        return (self.snake.getHead()[0] >= 0 and self.snake.getHead()[0] <= self.getRow() and self.snake.getHead()[1] >= 0 and self.snake.getHead()[1] <= self.getCol()) and boolean
    def validPositionSnake(self):
        return self.snake.getHead()[0] % 30 == 0 and self.snake.getHead()[1] % 30 == 0
    
    def drawOnBoard():
        pass
        
    def getBoardDirections(self):
        f =  30
        directions = {
            "right" : [f,0],
            "left" : [-f,0],
            "up" : [0, -f],
            "down" : [0,f]
        }
        return directions



    def moveSnakeHead(self, direction, prevDirection):
        directions = self.getBoardDirections()
        i = 0
        count = 0
        if len(self.snake.getCoordinates()) > 1:
        
            for i in range(len(self.snake.getCoordinates()) -1, 0, -1):
                self.snake.getCoordinates()[i] = self.snake.getCoordinates()[i-1][:]

            self.snake.changeCoordinateItem(0, directions[direction][0],directions[direction][1])


     
        else:
                
            
            x,y = self.snake.getHead()
            for i in range(len(self.snake.getCoordinates())  ):

                self.snake.changeCoordinateItem(i, directions[direction][0],directions[direction][1])
    
    
    # perhaps make the snake position hardcoded.
    def buildGrid(self):
        squareCount = 0
        maxX, maxY = self.getScreen().get_size()
        iterations = ((maxX // 30) * (maxY // 30)) # total number of loops
        randomIteration = random.randint(0, iterations)
        for i in range(0, maxX, 30):
            squareCount+=1
            for j in range(0, maxY, 30):
                currentIteration = int(((i*(maxX//30)) + j) / 30) # current loop number 
                
          
                square = Square(i,j, self.getScreen(), squareCount)
                
               
                square.drawSquare()


                squareCount+=1
        
        

        #if((self.snake.getHead() == self.food.getCoordinates()  )  or self.food.validCoordinates() == False):
            
        self.spawnFood()
    
    def spawnFood(self):
        [x,y] = self.food.getCoordinates() if self.food.getCoordinates() != [-1,-1] and self.checkCollision() == False else self.food.spawnFood(self.getRow(), self.getCol())
        
        self.food.setCoordinates([x,y])
        pygame.draw.rect(self.getScreen(), (255,0,0), pygame.Rect(x+7.5,y+7.5,15,15))

    def checkCollision(self):
        return self.snake.getCoordinates()[0] == self.food.getCoordinates()
    
    def addSnakePart(self, latestDirection):
        directions = self.getBoardDirections()
        lastNode = self.snake.getCoordinates()[-1]
        reference = list(directions.keys()).index(latestDirection)

        valid = reference+1 if reference % 2 == 0 else reference-1

        x,y = directions[list(directions)[valid]]
        


        self.snake.addCoordinates(lastNode[0]+(x*2), lastNode[1] + (y*2))

        

    def addSnake(self):

      
        #x,y = self.snake.getHead()



    
        for x,y in self.snake.getCoordinates():
            colour = (0,0, 200) if [x,y] == self.snake.getHead() else (0,0,255)
            pygame.draw.rect(self.getScreen(), (0,0,0), pygame.Rect(x-2,y-2,35,35))

            pygame.draw.rect(self.getScreen(), colour, pygame.Rect(x,y,30,30))

                
               
   



               
            