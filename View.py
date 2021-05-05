
from os import path, getcwd

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


iconPath = path.join(getcwd(), "icon\icon.ico")


class GraphUI(QDialog):
    def __init__(self, parent=None):
        super(GraphUI, self).__init__(parent)

        self.setWindowTitle("Graph Application")
        self.setWindowIcon(QIcon(iconPath))

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.generalLayout = QVBoxLayout()
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)

        self._createButtons()

        self.setLayout(self.generalLayout)

    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "Draw": (0, 0, 100, 40),
            "Read": (0, 1, 100, 40),
            "Algorithms": (0, 2, 100, 40),
            "Save": (0, 3, 100, 40),
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        self.generalLayout.addLayout(buttonsLayout)

    def getPathFile(self):
        pathFile = path.join(getcwd(), "input.txt")
        return pathFile

