
import game
import time_series_data
import numpy as np
import re
import os
from collections import Counter

num_of_iters = 30 
file_name = input("Path to game configuration : ")
c = input('Tactic for filtration plot : ')
path = os.path.join('examples/', file_name)

if re.search('examples/Simulated[1-9].txt', path):
    game_instance = game.SimulatedGame(path)
else :
    game_instance = game.Game(path) 
    print("game")


time_series_data_instance = time_series_data.time_series_data()
for time, state in game_instance:
    if (time > num_of_iters):
        break

    for line in state:
        print(' '.join(line)) 
    print('----------------------------------------')
    time_series_data_instance.update(state, time)

    # input()

VR_complexes = time_series_data_instance.seriesToComplexes(3, 3)

#print("--------------------")
#VR_complexes['T'].printFiltration(300)
#print("--------------------")

VR_complexes[c].plotPersistenceDiagram()

