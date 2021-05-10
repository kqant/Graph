from functools import partial
from sys import exit


class GraphCtrl:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._connectButtons()

    def _connectButtons(self):
        self.view.buttons["Draw"].clicked.connect(partial(self._drawGraph))
        self.view.buttons["Choose Input File"].clicked.connect(partial(self._chooseInputFile))
        self.view.buttons["Read"].clicked.connect(partial(self._readGraph))
        self.view.CheckBoxDirected.stateChanged.connect(partial(self._changeDir))
        self.view.CheckBoxWeighted.stateChanged.connect(partial(self._changeWeight))
        self.view.actionOpen.triggered.connect(partial(self._openGraph))
        self.view.actionSave.triggered.connect(partial(self._saveGraph))
        self.view.actionExit.triggered.connect(partial(self._exit))


    def _drawGraph(self):
        self._changeInputType()
        self.model.functions["chooseDrawType"](self)


    def _readGraph(self):
        self.model.graph.readGraph()


    def _changeInputType(self):
        self.model.graph._inputType = self.view.comboBoxInputType.currentText()


    def _chooseInputFile(self):
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self._readGraph()

    def _openGraph(self):
        self.model.graph.openGraph(self.view.getPathFile())
        self.setCheckBoxes()

    def setCheckBoxes(self):
        self.view.CheckBoxDirected.setChecked(self.model.graph._directed)
        self.view.CheckBoxWeighted.setChecked(self.model.graph._weighted)


    def _saveGraph(self):
        path = self.view.createNewFile()
        if path:
            self.model.graph.saveGraph(path)

    def _changeDir(self):
        self.model.graph._directed = self.view.CheckBoxDirected.isChecked()


    def _changeWeight(self):
        self.model.graph._weighted = self.view.CheckBoxWeighted.isChecked()

    def _exit(self):
        exit()