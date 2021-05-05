
from graph import Graph
from render import drawGraph


class GraphModel():
    def __init__(self):
        self.graph = Graph()
        self.functions = {
            drawGraph.__name__: drawGraph
        }

