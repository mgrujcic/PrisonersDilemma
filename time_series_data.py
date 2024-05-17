from Tactic import validTactics
from Complex import Complex, VRComplex

class time_series_data:
    def __init__(self):
        self.data = {}
        for tactic in validTactics:
            self.data[tactic] = []
            print(tactic)

    def update(self, state, time):
        for i in range(len(state)):
            for j in range ((len(state[i]))):
                tactic = state[i][j]
                self.data[tactic].append((i, j, time))
    
    def getData(self):
        return self.data

    def seriesToComplexes(self, max_edge_length, max_dimension):
        VR_complexes = {}
        for tactic, points in self.data.items():
            VR_complexes[tactic] = VRComplex(points, max_edge_length, max_dimension)
        return VR_complexes