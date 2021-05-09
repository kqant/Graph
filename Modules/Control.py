
from functools import partial


class GraphCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectButtons()

    def _connectButtons(self):
        self._view.buttons["Draw"].clicked.connect(partial(self._drawGraph))
        self._view.buttons["Choose Input File"].clicked.connect(partial(self._chooseInputFile))
        self._view.buttons["Save Graph"].clicked.connect(partial(self._saveGraph))
        self._view.CheckBoxDirected.stateChanged.connect(partial(self._changeDir))
        self._view.CheckBoxWeighted.stateChanged.connect(partial(self._changeWeight))

    def _drawGraph(self):
        self._changeInputType()
        self._model.graph.readGraph()
        self._model.functions["chooseDrawType"](self)

    def _changeInputType(self):
        self._model.graph._inputType = self._view.comboBoxInputType.currentText()

    def _chooseInputFile(self):
        filepath = self._view.getPathFile()
        self._model.graph.initGraphFile(filepath)

    def _saveGraph(self):
        print(self._saveGraph.__name__)

    def _changeDir(self):
        self._model.graph._directed = self._view.CheckBoxDirected.isChecked()

    def _changeWeight(self):
        self._model.graph._weighted = self._view.CheckBoxWeighted.isChecked()

