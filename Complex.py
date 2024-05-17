import gudhi as gd 
import time_series_data

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

    def printFiltration(self, num_of_elements):
        risp_list = list(self.getFiltration())
        for splx in risp_list[0:num_of_elements]:
            print(splx)