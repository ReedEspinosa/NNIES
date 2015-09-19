from animalClass import Animal
import numpy as np

beast = Animal([0, 0], 10, 1, 2, 20)

surroundings = np.zeros(18)
surroundings[1] = 1;
print beast.act(surroundings)