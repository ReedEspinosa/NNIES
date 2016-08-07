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

    # this defines how plant life growths over the course of a turn
    # the current formula is a scaled version of plank's BB radiation
    # T=0.5 -> growth of ~0.1/turn, leveling off ~3
    # T=2 -> growth of ~5/turn up, leveling off ~30
    def sigmoid(self, xIn, temp=1):
        if xIn == 0:
            return 0
        num = xIn**3
        denom = np.exp(xIn/temp) - 1
        growth = num/denom
        return xIn + growth

    # make list of eight surrounding and center plant life numbers
    def nine_surrounding_list(self, target_index):
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


    # this function evolves  the board
    # each element of the original board is evolved by
    # averaging the element with the 8 surround elements
    # and applying the above sigmoid to it to smooth and
    # group numbers
    # larger growth_factor means more growth (see above)
    def evolve_board(self, growth_factor=1, spread_rate=0.1):
        dimension = self.board.shape[0]
        blank_matrix = np.ones((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                surroundings = self.nine_surrounding_list((i, j))
                nghbrAvg = np.average(surroundings[1:])
                average = (surroundings[0] + spread_rate*nghbrAvg)/(1+spread_rate)
                sig = self.sigmoid(average, growth_factor)
                blank_matrix[i, j] = sig
        self.board = blank_matrix
        




