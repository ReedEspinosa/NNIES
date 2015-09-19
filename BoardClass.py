# import
import numpy as np

# define board class


class GameBoard(object):
    def __init__(self, initial_size):

        # board will be initial_Size x initial_Size
        self.initial_size = initial_size

        # create initial board
        self.board = np.ones((self.initial_size, self.initial_size))

    # creates a random setup for board initially
    def create_board(self, weight=1):
        r_matrix = np.random.rand(self.initial_size, self.initial_size)
        r_matrix_weighted = weight * r_matrix
        self.board = self.board + r_matrix_weighted

    # this evolves a single input with a sigmoid.  scale input defaults to 1
    def sigmoid(self, x, scale=1):
        num = 1 - x
        den = np.sqrt(1 + (1 - x) ** 2)
        frac = num / den
        output = x + (scale * frac) + 1
        return output

    # this function averages the item at the target_index with the 8
    # surrounding items. assumes square matrices only, assumes one
    # end of the board connects to other
    def eight_surrounding(self, input_matrix, target_index):
        dimension = input_matrix.shape[0]
        target_item = input_matrix.item(target_index)
        x = target_index[0]
        y = target_index[1]
        xp = np.mod(target_index[0] + 1, dimension)
        xm = np.mod(target_index[0] - 1, dimension)
        yp = np.mod(target_index[1] + 1, dimension)
        ym = np.mod(target_index[1] - 1, dimension)
        west = input_matrix.item(x, ym)
        northwest = input_matrix.item(xm, ym)
        north = input_matrix.item(xm, y)
        northeast = input_matrix.item(xm, yp)
        east = input_matrix.item(x, yp)
        southeast = input_matrix.item(xp, yp)
        south = input_matrix.item(xp, y)
        southwest = input_matrix.item(xp, ym)
        all_direction = [target_item, west, northwest, north, northeast,
                         east, southeast, south, southwest]
        return np.average(all_direction)

    # each element of the original board is evolved by
    # averaging the element with the 8 surround elements
    # and applying the above sigmoid to it to smooth and
    # group numbers
    #
    # this function evolves a general input board
    def evolve(self, input_matrix, growth_factor=1):
        dimension = input_matrix.shape[0]
        blank_matrix = np.ones((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                average = self.eight_surrounding(input_matrix, (i, j))
                sig = self.sigmoid(average, growth_factor)
                blank_matrix[i, j] = sig
        return blank_matrix

    # this function evolves the specific game board for this class
    def evolve_board(self, growth_factor=1):
        self.board = self.evolve(self.board, growth_factor)
