
from functools import partial


class GraphCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectButtons()

    def _drawButton(self):
        self._model.graph.getGraphX()
        # graphX = self._model.getFields()
        self._model.functions["drawGraph"](self._view, self._model.graph)

    def _readButton(self):
        filepath = self._view.getPathFile() # <- дайте путь до файла с графом из View(GUI)
        self._model.graph.initGraphFile(filepath)

    def _algorithmsButton(self):
        print(self._algorithmsButton.__name__)

    def _saveButton(self):
        print(self._saveButton.__name__)

    def _connectButtons(self):
        self._view.buttons["Draw"].clicked.connect(partial(self._drawButton))
        self._view.buttons["Read"].clicked.connect(partial(self._readButton))
        self._view.buttons["Algorithms"].clicked.connect(partial(self._algorithmsButton))
        self._view.buttons["Save"].clicked.connect(partial(self._saveButton))

