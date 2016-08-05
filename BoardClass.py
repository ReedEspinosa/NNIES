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
    # scaling determines how sparse the matrix is, should be
    # between 0 and 1.  For example, scale 0.6 means that
    # intial random values are 0 to 0.6 and rounding on average 
    # causes 1/6 of entries to become 1.
    def create_board(self, scale=1):
        r_matrix = np.random.rand(self.initial_size, self.initial_size)
        r_matrix_scaled = scale * r_matrix
        rounded_matrix = np.rint(r_matrix_scaled)
        self.board = rounded_matrix

    # this evolves a single input with a sigmoid.  scale input defaults to 1
    # method is defined such that plants "grow" increasingly less as they get larger
    def sigmoid(self, x_prime, scale1=1, scale2=1):
        x = x_prime / scale1
        num = 1 - x
        den = np.sqrt(1 + (x - 1) ** 2)
        frac = num / den
        output = x + (scale2 * frac) + 1
        return output

    # make list of eight surrounding plant life numbers
    def eight_surrounding_list(self, target_index):
        dimension = self.board.shape[0]
        target_item = self.board.item(target_index)
        x = target_index[0]
        y = target_index[1]
        xp = np.mod(target_index[0] + 1, dimension)
        xm = np.mod(target_index[0] - 1, dimension)
        yp = np.mod(target_index[1] + 1, dimension)
        ym = np.mod(target_index[1] - 1, dimension)
        west = self.board.item(x, ym)
        northwest = self.board.item(xm, ym)
        north = self.board.item(xm, y)
        northeast = self.board.item(xm, yp)
        east = self.board.item(x, yp)
        southeast = self.board.item(xp, yp)
        south = self.board.item(xp, y)
        southwest = self.board.item(xp, ym)
        all_direction = [target_item, west, northwest, north, northeast,
                         east, southeast, south, southwest]
        return all_direction

    # this function averages the item at the target_index with the 8
    # surrounding items. assumes square matrices only, assumes one
    # end of the board connects to other
    def eight_surrounding(self, target_index):
        l_list = self.eight_surrounding_list(target_index)
        return np.average(l_list)

    # this function evolves  the board
    # each element of the original board is evolved by
    # averaging the element with the 8 surround elements
    # and applying the above sigmoid to it to smooth and
    # group numbers
    # larger growth_factor means less growth
    def evolve_board(self, growth_factor=1):
        dimension = self.board.shape[0]
        blank_matrix = np.ones((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                average = self.eight_surrounding((i, j))
                sig = self.sigmoid(average, growth_factor)
                blank_matrix[i, j] = sig
        self.board = blank_matrix
        
