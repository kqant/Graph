
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from os import path, getcwd, utime

iconPath = path.join(getcwd(), "Icons/GraphDrawer.svg")


class GraphUI(QMainWindow):
    def __init__(self, parent = None):
        super(GraphUI, self).__init__(parent)
        self.setWindowTitle("GraphDrawer")
        self.setFixedSize(900, 600)
        self.setWindowIcon(QIcon(iconPath))
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.centralwidget = QWidget(self)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)

        self.buttonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.centralwidget)
        self.graphwidget = QWidget(self)
        self.generalLayout = QVBoxLayout(self.graphwidget)

        self._createButtons()
        self._createCanvas()
        self._createMinPathInput()
        self._createAlgoOutput()

        QMetaObject.connectSlotsByName(self)

        self._setObjectsNames()
        self._setGeometry()
        self.figure.clf()


    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "Input File": (0, 5, 105, 30),
            "⭯": (0, 70, 30, 30),
            "Coloring": (45, 5, 140, 45),
            "Min Path": (80, 5, 140, 45),
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            font = QFont()
            if btnText == "⭯":
                font.setPointSize(18)
            else:
                font.setPointSize(12)
            self.buttons[btnText].setFont(font)
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        self.buttonsLayout.addLayout(buttonsLayout)


    def _createCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)


    def _createMinPathInput(self):
        self.TextMinPathStart = QLineEdit(self.centralwidget)
        self.TextMinPathGoal = QLineEdit(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.TextMinPathStart.setFont(font)
        self.TextMinPathGoal.setFont(font)
        self.TextMinPathStart.setPlaceholderText("Start")
        self.TextMinPathGoal.setPlaceholderText("Goal")


    def _createAlgoOutput(self):
        font = QFont()
        font.setPointSize(11)
        self.AlgoOutput = QLineEdit(self.centralwidget)
        self.AlgoOutput.setText(f"Output:")


    def _setObjectsNames(self):
        self.setObjectName("MainWindow")
        self.centralwidget.setObjectName("centralwidget")
        self.graphwidget.setObjectName("graphwidget")
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.TextMinPathStart.setObjectName("TextMinPathStart")
        self.TextMinPathGoal.setObjectName("TextMinPathStart")
        self.AlgoOutput.setObjectName("AlgoOutput")


    def _setGeometry(self):
        self.centralwidget.setGeometry(0, 0, 900, 600)
        self.graphwidget.setGeometry(140, 0, 760, 590)
        self.horizontalLayoutWidget.setGeometry(QRect(5, 0, 140, 200))
        self.TextMinPathStart.setGeometry(QRect(15, 370, 50, 30))
        self.TextMinPathGoal.setGeometry(QRect(85, 370, 50, 30))
        self.AlgoOutput.setGeometry(35, 410, 80, 30)


    def getPathFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Graph Application", path.join(getcwd(), "input.txt"), options=options)
        if fileName:
            return fileName


    def showResult(self, type, result):
        msg = QMessageBox()
        if type == "Min Path Finding":
            msg.setWindowTitle("Min path result")
            msg.setText(f"Min path is {result}")
        elif type == "Coloring":
            msg.setWindowTitle("Coloring result")
            msg.setText(f"Colors number is {result}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


    def showError(self, error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setWindowTitle("Error")
        msg.setText(str(error))

        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

