# import
import numpy as np

# define board class


class GameBoard(object):
    def __init__(self, initial_size):

        # board will be initial_Size x initial_Size
        self.initial_size = initial_size

        # create initial board
        self.initial_Board = np.ones((self.initial_size, self.initial_size))

    # creates a random setup for board initially
    def create_board(self, weight):
        r_matrix = np.random.rand(self.initial_size, self.initial_size)
        r_matrix_weighted = weight * r_matrix
        self.board = self.initial_Board + r_matrix_weighted
