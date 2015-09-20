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
        self.herb_list = [Animal([np.random.randint(0, board_size),
                          np.random.randint(0, board_size)])
                          for count in xrange(herb_number)]

    # returns a list of the positions of all herbivores
    def herb_position_list(self):
        return [self.herb_list[i].cords
                for i in xrange(len(self.herb_list))]

    # for a given animal this creates a list of surroundings
    def surrounding_list(self, herb_obj):
        position = (herb_obj.cords[0], herb_obj.cords[1])
        land = self.land_map.board
        return self.land_map.eight_surrounding_list(land, position)

# TEST:
# game = OverallGame(10, 5)
# print game.land_map.board
# print game.herb_list[0].cords
# print game.herb_list[1].cords
# print game.herb_position_list()
# print game.surrounding_list(game.herb_list[1])
