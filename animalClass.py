# import
import numpy as np
from nueralnet_classes import nodeNet

# define board class
class Animal(object):
    def __init__(self, cords = [0, 0], life=10, visRange=1, visDim=2, symbols=20):
        self.cords = np.array(cords)
        self.life = life
        
        # nodeNet w/ input for each visDim over range, symbols nodes and 10 outputs
        inputs = visDim*np.power((1+2*visRange),2) # visDim x squares in vision range
        self.brainNet = nodeNet(inputs, symbols, 10) # one output for each square plus mate
        self.brainNet.mutate(0.5) # diversify initial population
        
    def decide(self, surroundings):
        options = self.brainNet.processInputs(surroundings)
        decision = options.argmax(0)
        if decision == 9: # reproduce
            repoFlag = 1
            self.life = self.life/2
            eastWest = 0
            northSouth = 0
        else:
            northSouth = np.floor(decision/3) - 1
            eastWest = decision%3 -1
            
        return np.array([northSouth, eastWest, repoFlag])
    
    def feed(self, foodAmount=0):
        self.life = self.life + foodAmount;
    
    
        