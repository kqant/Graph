
from algorithms.calc import calc

class GraphModel:
    def __init__(self):
        self.functions = {
            calc.__name__: calc
        }

