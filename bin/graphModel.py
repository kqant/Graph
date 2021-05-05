from .algorithms import *
from .input import *
import networkx as nx

class GraphModel():
    def __init__(self):
        self.functions = {
            drawGraph.__name__: drawGraph,
            getGraph.__name__: getGraph,
            saveGraph.__name__: saveGraph
        }