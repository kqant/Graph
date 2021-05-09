
from .Graph import Graph
from .Render import chooseDrawType


class GraphModel():
    def __init__(self):
        self.graph = Graph()
        self.functions = {
            chooseDrawType.__name__: chooseDrawType
        }

