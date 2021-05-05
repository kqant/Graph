from functools import partial


class GraphCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectButtons()
    
    def getRes(self, name):
        if name == "drawGraph":
            return partial(self._model.functions["drawGraph"], self._view)
        elif name == "getGraph":
            return partial(self._model.functions["getGraph"], "SPISOK SMEJNOSTY")
        elif name == "saveGraph":
            return partial(self._model.functions["saveGraph"])
        return self.nuTiLox
    
    def nuTiLox():
        print("Functsiya ne rabotaet, idi fixi")


    
    def _connectButtons(self):
        self._view.buttons["Draw"].clicked.connect(self.getRes("drawGraph"))
        self._view.buttons["Read"].clicked.connect(self.getRes("getGraph"))
        self._view.buttons["Save"].clicked.connect(self.getRes("saveGraph"))

