import game
import time_series_data
import numpy as np

num_of_iters = int(input("Number of game iterations : "))

time_series_data_instance = time_series_data.time_series_data()
for time, state in game.Game("random.txt"):
    if (time > num_of_iters):
        break

    #print(state)
    time_series_data_instance.update(state, time)
    # input()

VR_complexes = time_series_data_instance.seriesToComplexes(np.sqrt(2), 3)
VR_complexes['A'].printFiltration(300)
