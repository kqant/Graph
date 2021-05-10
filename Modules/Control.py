from functools import partial
from sys import exit


class GraphCtrl:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._connectButtons()

    def _connectButtons(self):
        self.view.buttons["Draw"].clicked.connect(partial(self.drawGraph))
        self.view.buttons["Choose Input File"].clicked.connect(partial(self.chooseInputFile))
        self.view.buttons["Read"].clicked.connect(partial(self.readGraph))
        self.view.CheckBoxDirected.stateChanged.connect(partial(self.changeDir))
        self.view.CheckBoxWeighted.stateChanged.connect(partial(self.changeWeight))
        self.view.actionOpen.triggered.connect(partial(self.openGraph))
        self.view.actionSave.triggered.connect(partial(self.saveGraph))
        self.view.actionExit.triggered.connect(partial(self.exit))


    def drawGraph(self):
        self.changeInputType()
        self.model.functions["chooseDrawType"](self)


    def readGraph(self):
        self.model.graph.readGraph()


    def changeInputType(self):
        self.model.graph._inputType = self.view.comboBoxInputType.currentText()


    def chooseInputFile(self):
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self.readGraph()

    def openGraph(self):
        self.model.graph.openGraph(self.view.getPathFile())
        self.setCheckBoxes()

    def setCheckBoxes(self):
        self.view.CheckBoxDirected.setChecked(self.model.graph.directed)
        self.view.CheckBoxWeighted.setChecked(self.model.graph.weighted)


    def saveGraph(self):
        path = self.view.createNewFile()
        if path:
            self.model.graph.saveGraph(path)

    def changeDir(self):
        self.model.graph.directed = self.view.CheckBoxDirected.isChecked()


    def changeWeight(self):
        self.model.graph.weighted = self.view.CheckBoxWeighted.isChecked()

    def exit(self):
        exit()