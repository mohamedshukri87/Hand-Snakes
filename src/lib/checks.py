import numpy as np

def checkSameLine(arr):
 
    

        nparr = np.array(arr)
        firstIndexes = nparr[:,0]
        secondIndexes = nparr[:,1]
        
        return len(set(firstIndexes)) == 1 or len(set(secondIndexes)) == 1