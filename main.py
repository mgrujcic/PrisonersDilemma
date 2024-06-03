
import game
import time_series_data
import numpy as np
from collections import Counter

num_of_iters = 30 #int(input("Number of game iterations : "))

time_series_data_instance = time_series_data.time_series_data()
for time, state in game.Game("examples/Case2.txt"):
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

VR_complexes['D'].plotPersistenceDiagram()

