class Snake:
    def __init__(self, initX, initY):
        self.initX = initX
        self.initY = initY
        self.head = [initX, initY]
        self.coordinates = [[self.initX, self.initY]]
        

    def getHead(self):
        return self.coordinates[0]
    
    def changeHead(self, x, y):
        
        self.head = [x,y]
        

    def changeCoordinates(self, x, y):

        arr = []

        for a,b in self.getCoordinates():
            a+=x
            b+=y

            arr.append([a,b])
            
            self.setCoordinates(arr)

    def changeCoordinateItem(self, itemNumber, x, y):

        self.getCoordinates()[itemNumber] = [self.getCoordinates()[itemNumber][0] + x, self.getCoordinates()[itemNumber][1] + y]

    def addCoordinates(self, x , y):
        self.getCoordinates().append([x,y])
    def setCoordinates(self, arr):
        self.coordinates = arr
    def getCoordinates(self):
        return self.coordinates
    
    def checkSameLine(self):
        return all(self.getCoordinates()[0] == self.getCoordinates()[0][0] for row in self.getCoordinates()) or all(self.getCoordinates()[1] == self.getCoordinates()[0][1] for row in self.getCoordinates())


    