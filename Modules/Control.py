from functools import partial
from sys import exit


class GraphCtrl:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._connectButtons()

    def _connectButtons(self):
        self.view.buttons["Draw"].clicked.connect(partial(self.chooseGraphToDraw))
        self.view.buttons["Choose Input File"].clicked.connect(partial(self.chooseInputFile))
        self.view.buttons["Read"].clicked.connect(partial(self.readGraph))
        self.view.CheckBoxDirected.stateChanged.connect(partial(self.changeDir))
        self.view.CheckBoxWeighted.stateChanged.connect(partial(self.changeWeight))
        self.view.actionOpen.triggered.connect(partial(self.openGraph))
        self.view.actionSave.triggered.connect(partial(self.saveGraph))
        self.view.actionExit.triggered.connect(partial(self.exit))


    def chooseGraphToDraw(self):
        self.changeInputType()
        algoUse = self.view.comboBoxAlgo.currentText()
        figure, canvas, adj, directed, weighted = \
        self.view.figure, self.view.canvas, self.model.graph.adj, self.model.graph.directed, self.model.graph.weighted
        if algoUse == "Default":
            self.model.functions["drawDefault"](figure, canvas, adj, directed, weighted)
        
        elif algoUse == "Min Path Finding":
            ok = self.view.minPathTakeInput()
            if ok == "Doesn't exist vertice":
                self.view.showError(ok)
                return
            start, goal = ok
            ok = self.model.graph.minPathFind(start, goal)
            if ok == "Vertices not in graph" or ok == "Minimal path error":
                self.view.showError(ok)
                print("path error")
                return
            length, path = ok
            self.model.functions["drawMinPath"](figure, canvas, adj, directed, weighted, path)
        
        elif algoUse == "Coloring":
            colors = self.model.graph.coloring()
            self.model.functions["drawColoring"](figure, canvas, adj, directed, weighted, colors)


    def readGraph(self):
        ok = self.model.graph.readGraph()
        if ok == "File not match input type" or ok == "Path error":
            self.view.showError(ok)
            return


    def changeInputType(self):
        self.model.graph._inputType = self.view.comboBoxInputType.currentText()


    def chooseInputFile(self):
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self.readGraph()

    def openGraph(self):
        ok = self.model.graph.importGraph(self.view.getPathFile())
        if ok == "File corrupted":
            self.view.showError(ok)
            return
        self.setCheckBoxes()

    def setCheckBoxes(self):
        self.view.CheckBoxDirected.setChecked(self.model.graph.directed)
        self.view.CheckBoxWeighted.setChecked(self.model.graph.weighted)


    def saveGraph(self):
        path = self.view.createNewFile()
        if path:
            self.model.graph.exportGraph(path)

    def changeDir(self):
        self.model.graph.directed = self.view.CheckBoxDirected.isChecked()


    def changeWeight(self):
        self.model.graph.weighted = self.view.CheckBoxWeighted.isChecked()

    def exit(self):
        exit()