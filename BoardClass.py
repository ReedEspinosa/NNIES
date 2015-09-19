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

    # this evolves a single input with a sigmoid.  scale input defaults to 1
    def sigmoid(self, input, scale=1):
        num = 1 - input
        den = np.sqrt(1 + (1 - input) ** 2)
        frac = num / den
        output = input + (scale * frac) + 1
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
