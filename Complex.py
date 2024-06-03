import gudhi as gd 
import time_series_data
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter

class Complex:
    def __init__(self):
        pass 
    def getFiltration(self):
        pass

    def getDimension(self):
        pass

class VRComplex(Complex):
    def __init__(self, points, max_edge_length, max_dimension): 
        super().__init__
        self.skeleton = gd.RipsComplex(points = points, max_edge_length = max_edge_length)
        self.rips_simplex_tree = self.skeleton.create_simplex_tree(max_dimension) 

    def getFiltration(self):
        return self.rips_simplex_tree.get_filtration()

    def getDimension(self):
        return self.rips_simplex_tree.dimension()

    def getNumOfVertices(self):
        return self.rips_simplex_tree.num_vertices()

    def getNumOfSimplices(self):
        return self.rips_simplex_tree.num_simplices()

    def getPersistence(self):
        return self.rips_simplex_tree.persistence()

    def printFiltration(self, num_of_elements):
        print(f"ok: {self.getNumOfSimplices()}")
        risp_list = list(self.getFiltration())
        for splx in risp_list[0:num_of_elements]:
            print(splx)

    def plotPersistenceDiagram(self):
        class_color = [(1,0,0), (0,1,0), (0.7, 0.3, 0.1)]
        c = Counter(self.getPersistence())
        widths = []
        lefts = []
        labels = []
        colors = []
        for ((dim, (birth, death)), count) in c.items():
            widths.append(death - birth if not death == float('inf') else 5-birth)
            lefts.append(birth)
            colors.append(class_color[dim])
    
            labels.append(str(count))

        #print(widths)
        #print(lefts)
        fig, ax = plt.subplots()
        bars = ax.barh(y = range(0, len(widths)), width= widths, left=lefts, color=colors)

        for bar, left_border, label in zip(bars, lefts, labels):
            widths = left_border
            ax.text(widths, bar.get_y() + bar.get_height() / 2, label, va='center')

        custom_legend = [mpatches.Patch(color=color, label=label) for color, label in zip(class_color, [0, 1, 2])]
        ax.legend(handles=custom_legend, title='Dimension', loc='best')
        labels = [str(i) for i in range(5)] + ['inf']
        plt.xticks(range(6), labels=labels)

        plt.show()