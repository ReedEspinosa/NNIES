from animalClass import Animal
import numpy as np

beast = Animal([0, 0], 10, 1, 2, 20)

surroundings = np.zeros(18)
surroundings[1] = 1
print "-----------"
print "deltaLives: %d" %(beast.act(surroundings, [100, 100]))
print "new location: (%d,%d)" %(beast.cords[0], beast.cords[1])
print "new life: %f" %(beast.life)
print "-----------"