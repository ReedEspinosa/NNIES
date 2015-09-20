import numpy as np
from nueralnet_classes import nodeNet
from BoardClass import GameBoard
from animalClass import Animal

# this class runs the overall game


class OverallGame(object):
    def __init__(self, board_size, herb_number):

        # create a board object
        self.land_map = GameBoard(board_size)

        # create initial list of herbivores
        self.animal_list = [Animal([np.random.randint(0, board_size),
                            np.random.randint(0, board_size)])
                            for count in xrange(herb_number)]

game = OverallGame(10, 5)