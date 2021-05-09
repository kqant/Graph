from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from os import path, getcwd

iconPath = path.join(getcwd(), "icon/icon.ico")

class GraphUI(QMainWindow):
    def __init__(self, parent = None):
        super(GraphUI, self).__init__(parent)
        self.setWindowTitle("GraphDrawer")
        self.setFixedSize(900, 600)
        self.setWindowIcon(QIcon(iconPath))
        self.centralwidget = QWidget(self)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)

        self.buttonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.centralwidget)
        self.graphwidget = QWidget(self)
        self.generalLayout = QVBoxLayout(self.graphwidget)

        self._createButtons() # основные кнопки
        self._createInputTypeChoose()
        self._createInputTypeComboBox()
        self._createAlgoLabelChoose()
        self._createAlgoComboBox()
        self._createChooseProperties()
        self._createPropertiesCheckboxes()
        self._createMenuBar()
        self._createCanvas()

        QMetaObject.connectSlotsByName(self)

        self._setObjectsNames()
        self._setText()
        self._setGeometry()
        self.setLayout(self.generalLayout)


    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "Draw": (0, 0, 260, 100),
            "Choose Input File": (0, 2, 260, 100),
            "Save Graph": (0, 4, 260, 100),
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            font = QFont()
            font.setPointSize(18)
            self.buttons[btnText].setFont(font)
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        self.buttonsLayout.addLayout(buttonsLayout)


    def _createInputTypeChoose(self):
        self.ChooseInputType = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseInputType.setFont(font)
        self.ChooseInputType.setTextFormat(Qt.PlainText)
        self.ChooseInputType.setAlignment(Qt.AlignCenter)


    def _createInputTypeComboBox(self):
        self.comboBoxInputType = QComboBox(self.centralwidget)
        font = QFont()
        font.setPointSize(9)
        self.comboBoxInputType.setFont(font)
        self.comboBoxInputType.addItem("")
        self.comboBoxInputType.addItem("")


    def _createAlgoLabelChoose(self):
        self.ChooseAlgoritmnLabel = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseAlgoritmnLabel.setFont(font)
        self.ChooseAlgoritmnLabel.setTextFormat(Qt.PlainText)
        self.ChooseAlgoritmnLabel.setAlignment(Qt.AlignCenter)


    def _createAlgoComboBox(self):
        self.comboBoxAlgo = QComboBox(self.centralwidget)
        font = QFont()
        font.setPointSize(9)
        self.comboBoxAlgo.setFont(font)
        self.comboBoxAlgo.addItem("")
        self.comboBoxAlgo.addItem("")
        self.comboBoxAlgo.addItem("")


    def _createChooseProperties(self):
        self.ChooseProperties = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseProperties.setFont(font)
        self.ChooseProperties.setTextFormat(Qt.PlainText)
        self.ChooseProperties.setAlignment(Qt.AlignCenter)


    def _createPropertiesCheckboxes(self):
        self.CheckBoxDirected = QCheckBox(self.centralwidget)
        self.CheckBoxWeighted = QCheckBox(self.centralwidget)


    def _createMenuBar(self):
        self.widget = QWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.statusbar = QStatusBar(self)
        self.menuGraph = QMenu(self.menubar)
        self.actionNew = QAction(self)
        self.actionOpen = QAction(self)
        self.actionSave = QAction(self)

        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)
        self.menuGraph.addAction(self.actionNew)
        self.menuGraph.addAction(self.actionOpen)
        self.menuGraph.addAction(self.actionSave)
        self.menubar.addAction(self.menuGraph.menuAction())


    def _createCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)


    def _setObjectsNames(self):
        self.setObjectName("MainWindow")
        self.centralwidget.setObjectName("centralwidget")
        self.widget.setObjectName("widget")
        self.menubar.setObjectName("menubar")
        self.menuGraph.setObjectName("menuGraph")
        self.statusbar.setObjectName("statusbar")
        self.actionNew.setObjectName("actionNew")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave.setObjectName("actionSave")
        self.graphwidget.setObjectName("graphwidget")
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonsLayout.setObjectName("horizontalLayout_2")
        self.ChooseInputType.setObjectName("Choose input type")
        self.comboBoxInputType.setObjectName("Combo Box Input Type")
        self.ChooseAlgoritmnLabel.setObjectName("ChooseAlgoLabel")
        self.comboBoxAlgo.setObjectName("Combo Box Algo")
        self.ChooseProperties.setObjectName("ChooseProperties")
        self.CheckBoxDirected.setObjectName("CheckBoxDirected")
        self.CheckBoxWeighted.setObjectName("CheckBoxWeighted")



    def _setGeometry(self):
        self.centralwidget.setGeometry(0, 0, 900, 600)
        self.widget.setGeometry(QRect(150, 110, 750, 450))
        self.menubar.setGeometry(QRect(0, 0, 904, 21))
        self.graphwidget.setGeometry(180, 130, 700, 450)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 900, 100))
        self.ChooseInputType.setGeometry(QRect(20, 120, 150, 30))
        self.comboBoxInputType.setGeometry(QRect(20, 160, 150, 30))
        self.ChooseAlgoritmnLabel.setGeometry(QRect(20, 200, 150, 30))
        self.comboBoxAlgo.setGeometry(QRect(20, 240, 150, 30))
        self.ChooseProperties.setGeometry(QRect(20, 280, 150, 30))
        self.CheckBoxDirected.setGeometry(QRect(20, 320, 91, 21))
        self.CheckBoxWeighted.setGeometry(QRect(20, 340, 91, 21))


    def _setText(self):
        self.CheckBoxWeighted.setText("Weighted")
        self.comboBoxInputType.setItemText(0, "Adjacency List")
        self.comboBoxInputType.setItemText(1, "Adjacency Matrix")

        self.comboBoxAlgo.setItemText(0, "Default")
        self.comboBoxAlgo.setItemText(1, "Min Path Finding")
        self.comboBoxAlgo.setItemText(2, "Coloring")
        
        self.ChooseAlgoritmnLabel.setText("Choose algorithm")
        self.ChooseInputType.setText("Choose input type")

        self.CheckBoxDirected.setText("Directed")
        self.ChooseProperties.setText("Choose properties")

        self.menuGraph.setTitle("Graph")
        self.actionNew.setText("New")
        self.actionOpen.setText("Open")
        self.actionSave.setText("Save")

    def getPathFile(self):
        return QFileDialog.getOpenFileName()[0]


