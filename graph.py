
import numpy as np


class Graph():
    def __init__(self):
        pass

    def convert_matrix_to_list(self, matrix):
        G = {}
        for a in range(len(matrix)):
            for b in range(len(matrix)):
                if matrix[a][b]:
                    if a + 1 not in G:
                        G[a + 1] = {b + 1: matrix[a][b]}
                    else:
                        G[a + 1][b + 1] = matrix[a][b]
        return G

    def getGraphX(self):
        pass

    def initGraphFile(self, filepath):
        print(filepath)



if __name__ == "__main__":
    pass

