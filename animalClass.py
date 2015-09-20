# import
import numpy as np
from nueralnet_classes import nodeNet

# define board class
class Animal(object):
    def __init__(self, cords = [0, 0], life=10, visRange=1, visDim=2, symbols=20):
        self.cords = np.array(cords) # (y, x).. but we are symetric under 90deg rotation
        self.life = life
        
        # nodeNet w/ input for each visDim over range, symbols nodes and 10 outputs
        inputs = visDim*np.power((1+2*visRange),2) + 1 # visDim x squares in vision range + life
        self.brainNet = nodeNet(inputs, symbols, 10) # one output for each square plus mate
        self.brainNet.mutate(0.5) # diversify initial population
        
    def act(self, surroundings, boardSize):
        netInput = np.append(surroundings, self.life)
        options = self.brainNet.processInputs(netInput)
        decision = options.argmax(0)
        if decision == 9: # reproduce
            deltaLives = 1
            self.life = (self.life -1)/2
        else:
            deltaLives = 0
            deltaCord = [np.floor(decision/3) - 1, decision%3 -1] 
            self.cords = np.sum(self.cords, deltaCord) # move by decided amount
            self.cord = np.fmod(self.cords, boardSize) # wrap space     
            distance = np.sqrt(np.sum(np.abs(deltaCord)))
            self.life = self.life - distance - 1 # pay 1 for turn + distance traveled
        if self.life <= 0:
            deltaLives = -1
            
        return deltaLives
    
        