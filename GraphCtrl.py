
from functools import partial

class GraphCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectButtons()

    def _calculateResult(self):
        result = self._model.functions["calc"](self._view.displayExpressionText())
        self._view.setDisplayResultText(result)

    def _connectButtons(self):
        self._view.buttons["DAROVA"].clicked.connect(partial(self._calculateResult))

