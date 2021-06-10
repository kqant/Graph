
"""
Модуль контроллера (Controller) интерпретирует действия пользователя
из представления (View), оповещая модель (Model) о необходимости изменений.
"""



from functools import partial


class GraphCtrl:
    """
    Класс контроллера (Controller).

    Args:
        _view (GraphUI): экземпляр класса 'GraphUI' (View).
        _model (GraphModel): экземпляр класса 'GraphModel' (Model).

    Attributes:
        view (GraphUI): экземпляр класса 'GraphUI' (View).
        model (GraphModel): экземпляр класса 'GraphModel' (Model).
    """
    def __init__(self, _view, _model):       
        self.view = _view
        self.model = _model
        self._connectButtons()


    def _connectButtons(self):
        """Подключение кнопок графического интерфейса."""
        self.view.buttons["Input File"].clicked.connect(partial(self._chooseInputFile))
        self.view.buttons["⭯"].clicked.connect(partial(self._updateGraph))
        self.view.buttons["Clear"].clicked.connect(partial(self._clearGraph))
        self.view.buttons["Coloring"].clicked.connect(partial(self._coloringGraph))
        self.view.buttons["Min Path"].clicked.connect(partial(self._minPathGraph))
        self.view.aboutButton.clicked.connect(partial(self._aboutAuthors))


    def _chooseInputFile(self):
        """Выбор входного файла из view и передача пути в model."""
        filepath = self.view.getPathFile()
        if filepath:
            self.model.graph.initGraphFile(filepath)
            self.view.buttons["⭯"].setEnabled(True)
            self.view.statusBar().showMessage(filepath)
            self._updateGraph()


    def _updateGraph(self):
        """Инициализация графа из файла (model) и отображение в UI (view)."""
        try:
            self.model.graph.readGraph()
        except Exception as ex:
            self.view.showError(ex)
            return

        adj, dir, w = self.model.graph.getFields()

        self.view.figure.clf()
        self.model.functions["drawDefault"](adj, dir, w)
        self.view.canvas.draw()


    def _clearGraph(self):
        """Очистка графа во view и model."""
        self.model.graph.clearGraph()
        self.view.figure.clf()
        self.view.canvas.draw()
        self.view.statusBar().showMessage("Choose input file")
        self.view.buttons["⭯"].setEnabled(False)


    def _coloringGraph(self):
        """Нахождение цветов графа (model) и их графическое представление (view)."""
        try:
            q, colors = self.model.graph.coloring()
        except Exception as ex:
            self.view.AlgoOutput.setText(str(ex))
            return

        self.view.AlgoOutput.setText("Colors: " + str(q))

        adj, dir, w = self.model.graph.getFields()

        self.view.figure.clf()
        self.model.functions["drawColoring"](adj, dir, w, colors)
        self.view.canvas.draw()


    def _minPathGraph(self):
        """
        Нахождение кратчайшего пути графа и его графическое представление (view).

        Raises:
            Exception: "Fields error"
        """
        start, goal = self.view.TextMinPathStart.text(), self.view.TextMinPathGoal.text()

        try:
            if not start or not goal:
                raise Exception("Fields error")
            lenght, path = self.model.graph.minPathFind(start, goal)
        except Exception as ex:
            self.view.AlgoOutput.setText(str(ex))
            return

        self.view.AlgoOutput.setText("Min path: " + str(lenght))

        adj, dir, w = self.model.graph.getFields()

        self.view.figure.clf()
        self.model.functions["drawMinPath"](adj, dir, w, path)
        self.view.canvas.draw()


    def _aboutAuthors(self):
        """Вызов окошка с информацией об авторах."""
        self.view.aboutAuthors()

