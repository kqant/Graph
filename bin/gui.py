
import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

iconPath = os.path.join(os.getcwd(), "..\Icon\icon.ico")

class Gag(QMainWindow):
    def __init__(self, parent=None):
        super(Gag, self).__init__(parent)
        self.setWindowTitle("Graph")
        # self.setFixedSize(780, 673)
        self.setFixedSize(1024, 768)
        self.setWindowIcon(QIcon(iconPath))
        
        self.generalLayout = QVBoxLayout()
        self._buttons = QWidget(self)
        self.setCentralWidget(self._buttons)
        self.setLayout(self.generalLayout)
        self._buttons.setLayout(self.generalLayout)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)
        self._createButtons()
        # layout.addWidget(self.button)


    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "Draw": (0, 0, 100, 40),
            "Read": (0, 1, 100, 40),
            # "ChooseAlgorithm": (0, 2, 100, 40),
            "Save": (0, 3, 100, 40),
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        
        # self.setLayout(buttonsLayout)
        self.generalLayout.addLayout(buttonsLayout)
        



if __name__ == "__main__":
    graph = QApplication(sys.argv)
    
    view = Gag()

    view.show()
    sys.exit(graph.exec())
