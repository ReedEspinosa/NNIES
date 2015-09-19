# import
import numpy as np

# define board class


class GameBoard(object):
    def __init__(self, initial_size):

        # board will be initial_Size x initial_Size
        self.initial_Size = initial_size

        # create initial board
        self.initial_Board = np.ones((initial_size, initial_size))

    # creates a random setup for board initially
    def create_Board(self, weight):
    	

