
import numpy as np


class Graph:
    _adj: dict
    _directed: bool
    _weighted: bool
    _filePath: str
    _inputType: str


    def __init__(self, directed=False, weighted=False):
        self._adj = {}
        self._directed = directed
        self._weighted = weighted
        self._inputType = "adj list"
        self._filePath = "input.txt"

    def print(self):
        for key, value in self._adj.items():
            print(f"[{key}] -> ", end="")
            if value == set():
                print("{}")
            else:
                print(f"{value}")

    def addVertices(self, *verts):
        for v in verts:
            if v not in self._adj.keys():
                self._adj[v] = {}

    def addEdges(self, start, ends):
        self.addVertices(*range(1, max(start, *ends)+1))
        self._adj[start] = {**self._adj[start], **ends}
        
        if not self._directed:  # if underected
            for end in ends.keys():
                if end in self._adj.keys():
                    self._adj[end] = {**self._adj[end], **{start: 1}}
                else:
                    self._adj[end] = {start: 1}

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

    def readGraph(self, type):
        try:
            with open(self._filePath, "r") as fin:
                # Read graph as adjacency list
                print(f"File on path {self._filePath} is opened.")
                if type == "adj list":
                    while True:
                        temp = [int(i) for i in fin.readline().split()]
                        if temp == []:
                            break
                        if self._weighted:
                            for i in range(0, len(temp), 3):
                                self.addEdges(temp[i], {temp[i+1]:temp[i+2]})
                        else:
                            for i in range(0, len(temp), 2):
                                self.addEdges(temp[i], {temp[i+1]:1})
                # Read graph as adjacency matrix
                elif type == "adj matrix":
                    pass
        except FileNotFoundError:
            print("Path error")

    def initGraphFile(self, filepath):
        self._filePath = filepath
        self.readGraph(self._inputType)



if __name__ == "__main__":
    g = Graph(directed=True)
    g.readGraph()
    g.print()
    g.addVertices(3, 4, 5, 6)
    g.addEdges(7, {2:1, 3:1, 4:1})
    print("\n")
    g.print()

