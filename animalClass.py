# import
import numpy as np
from nueralnet_classes import nodeNet

# define board class
class Animal(object):
    def __init__(self, cords = [0, 0], life=10, visRange=1, visDim=2, symbols=20):
        self.cords = np.array(cords) # (y, x).. but we are symmetric under 90deg rotation
        self.life = np.float32(life)
        
        # nodeNet w/ input for each visDim over range, symbols nodes and 10 outputs
        self.Ninputs = visDim*np.power((1+2*visRange),2) + 1 # visDim x squares in vision range + life
        self.brainNet = nodeNet(self.Ninputs, symbols, 10) # one output for each square plus mate
        self.brainNet.mutate(0.5) # diversify initial population
        
    def act(self, surroundings, boardSize):
        if np.size(surroundings) != (self.Ninputs - 1):
            buf = "surroundings had %d elements but %d is expected" % (np.size(surroundings), self.Ninputs - 1)
            raise Exception(buf)
        netInput = np.append(surroundings, self.life)
        options = self.brainNet.processInputs(netInput)
        decision = options.argmax(0)
        if decision == 9: # wants to reproduce reproduce
            deltaLives = 1
            self.life = (self.life -1)/2
        else: # we are going to potentially move somewhere
            deltaLives = 0
            deltaCord = np.int_([np.floor(decision/3) - 1, decision%3 -1]) 
            self.cords = np.add(self.cords, deltaCord) # move by decided amount
            self.cords = np.mod(self.cords, boardSize) # wrap space     
            distance = np.sqrt(np.sum(np.abs(deltaCord)))
            self.life = self.life - distance - 1 # pay 1 for turn + distance traveled
        if self.life <= 0: # this beast is dead
            deltaLives = -1
            
        return deltaLives
    
        