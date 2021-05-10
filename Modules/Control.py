from functools import partial
from sys import exit


class GraphCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectButtons()

    def _connectButtons(self):
        self._view.buttons["Draw"].clicked.connect(partial(self._drawGraph))
        self._view.buttons["Choose Input File"].clicked.connect(partial(self._chooseInputFile))
        self._view.buttons["Read"].clicked.connect(partial(self._readGraph))
        self._view.CheckBoxDirected.stateChanged.connect(partial(self._changeDir))
        self._view.CheckBoxWeighted.stateChanged.connect(partial(self._changeWeight))
        self._view.actionOpen.triggered.connect(partial(self._openGraph))
        self._view.actionSave.triggered.connect(partial(self._saveGraph))
        self._view.actionExit.triggered.connect(partial(self._exit))


    def _drawGraph(self):
        self._changeInputType()
        self._model.functions["chooseDrawType"](self)


    def _readGraph(self):
        self._model.graph.readGraph()


    def _changeInputType(self):
        self._model.graph._inputType = self._view.comboBoxInputType.currentText()


    def _chooseInputFile(self):
        filepath = self._view.getPathFile()
        if filepath:
            print("AZAZ")
            self._model.graph.initGraphFile(filepath)
            self._readGraph()

    def _openGraph(self):
        self._model.graph.openGraph(self._view.getPathFile())
        self.setCheckBoxes()

    def setCheckBoxes(self):
        self._view.CheckBoxDirected.setChecked(self._model.graph._directed)
        self._view.CheckBoxWeighted.setChecked(self._model.graph._weighted)


    def _saveGraph(self):
        path = self._view.createNewFile()
        if path:
            self._model.graph.saveGraph(path)

    def _changeDir(self):
        self._model.graph._directed = self._view.CheckBoxDirected.isChecked()


    def _changeWeight(self):
        self._model.graph._weighted = self._view.CheckBoxWeighted.isChecked()

    def _exit(self):
        exit()