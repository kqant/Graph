
from functools import partial


class GraphCtrl:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._connectButtons()


    def _connectButtons(self):
        self.view.buttons["Input File"].clicked.connect(partial(self._chooseInputFile))
        self.view.buttons["⭯"].clicked.connect(partial(self._updateGraph))
        self.view.buttons["Coloring"].clicked.connect(partial(self._coloringGraph))
        self.view.buttons["Min Path"].clicked.connect(partial(self._minPathGraph))


    def _chooseInputFile(self):
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self._updateGraph()


    def _updateGraph(self):
        try:
            self.model.graph.readGraph()
        except Exception as ex:
            self.view.showError(ex)
            return

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model.functions["drawDefault"](adj, dir, w)
        self.view.canvas.draw()


    def _coloringGraph(self):
        q, colors = self.model.graph.coloring()

        self.view.AlgoOutput.setText(str(q))

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model.functions["drawColoring"](adj, dir, w, colors)
        self.view.canvas.draw()


    def _minPathGraph(self):
        start, goal = self.view.TextMinPathStart.text(), self.view.TextMinPathGoal.text()

        try:
            lenght, path = self.model.graph.minPathFind(start, goal)
        except Exception as ex:
            self.view.showError(ex)
            return

        self.view.AlgoOutput.setText(str(lenght))

        adj, dir, w = self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted

        self.view.figure.clf()
        self.model.functions["drawMinPath"](adj, dir, w, path)
        self.view.canvas.draw()

