import numpy as np
from copy import deepcopy
from nueralnet_classes import nodeNet
from BoardClass import GameBoard
from animalClass import Animal

# this class runs the overall game
class OverallGame(object):
    def __init__(self, board_size, herb_number):

        # create a board object
        self.land_map = GameBoard(board_size)
        self.board_size = board_size

        # create initial list of herbivores
        self.herb_list = [Animal([np.random.randint(0, board_size),
                          np.random.randint(0, board_size)])
                          for count in xrange(herb_number)]
        self.N_herbs = herb_number

    # returns a list of the positions of all herbivores
    def herb_position_list(self):
        return [self.herb_list[i].cords for i in xrange(self.N_herbs)]

    # for a given animal this creates a list of surroundings
    def surrounding_list(self, herb_obj):
        position = (herb_obj.cords[0], herb_obj.cords[1])
        return self.land_map.nine_surrounding_list(position)

    # evolve the game one turn
    def executeTurn(self):
        herb_i = 0
        self.land_map.evolve_board(1)
        while herb_i < self.N_herbs):
            surroundings = self.surrounding_list(self.herb_list[herb_i])
            chng = self.herb_list[herb_i].act(surroundings, self.board_size)
            self.land_map.board[self.herb_list[herb_i].cords] = 0 # they ate everything
            if chng == 1:
                # add a new herb
                x.herb_list.append(deepcopy(x.herb_list[herb_i]))
                self.herb_list[self.N_herbs].brainNet.mutate(0.05)
                self.N_herbs = self.N_herbs + 1
                print("Birth!")
                herb_i += 1
            elif chng == -1:
                # kill this herb
                self.herb_list.pop(herb_i)
                self.N_herbs = self.N_herbs - 1
                print("Death!")
            else:
                herb_i += 1
                
    # method to display board...
                          

# TEST:
# game = OverallGame(10, 5)
# print game.land_map.board
# print game.herb_list[0].cords
# print game.herb_list[1].cords
# print game.herb_position_list()
# print game.surrounding_list(game.herb_list[1])
