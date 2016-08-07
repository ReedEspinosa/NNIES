# this looks reasonable at first but then it settles on a signle population
# the number is  settles on is constant and doesn't change at all

from overallGameClass import OverallGame

game = OverallGame(100, 200)

for i in xrange(500):
    print(i, game.N_herbs)
    game.executeTurn(1, 0.1)
