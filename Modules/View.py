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

        self.createButtons()
        self.createInputTypeChoose()
        self.createInputTypeComboBox()
        self.createAlgoLabelChoose()
        self.createAlgoComboBox()
        self.createChooseProperties()
        self.createPropertiesCheckboxes()
        self.createMenuBar()
        self.createCanvas()
        self.createMinPathInput()
        self.createAlgoOutput()

        QMetaObject.connectSlotsByName(self)

        self.setObjectsNames()
        self.setText()
        self.setGeometry()
        self.figure.clf()




    def createButtons(self):
        self.buttons = {}
        buttons = {
            "Input File": (0, 5, 105, 30),
            "⭯": (0, 70, 30, 30),
            "Draw": (45, 5, 140, 55),
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

    def createMinPathInput(self):
        self.TextMinPathStart = QLineEdit(self.centralwidget)
        self.TextMinPathGoal = QLineEdit(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.TextMinPathStart.setFont(font)
        self.TextMinPathGoal.setFont(font)
        self.TextMinPathStart.setPlaceholderText("Start")
        self.TextMinPathGoal.setPlaceholderText("Goal")


    def createAlgoOutput(self):
        font = QFont()
        font.setPointSize(11)
        self.AlgoOutput = QLineEdit(self.centralwidget)
        self.AlgoOutput.setText(f"Output:")

    def createInputTypeChoose(self):
        self.ChooseInputType = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseInputType.setFont(font)
        self.ChooseInputType.setTextFormat(Qt.PlainText)
        self.ChooseInputType.setAlignment(Qt.AlignCenter)


    def createInputTypeComboBox(self):
        self.comboBoxInputType = QComboBox(self.centralwidget)
        font = QFont()
        font.setPointSize(9)
        self.comboBoxInputType.setFont(font)
        self.comboBoxInputType.addItem("")
        self.comboBoxInputType.addItem("")


    def createAlgoLabelChoose(self):
        self.ChooseAlgoritmnLabel = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseAlgoritmnLabel.setFont(font)
        self.ChooseAlgoritmnLabel.setTextFormat(Qt.PlainText)
        self.ChooseAlgoritmnLabel.setAlignment(Qt.AlignCenter)


    def createAlgoComboBox(self):
        self.comboBoxAlgo = QComboBox(self.centralwidget)
        font = QFont()
        font.setPointSize(9)
        self.comboBoxAlgo.setFont(font)
        self.comboBoxAlgo.addItem("")
        self.comboBoxAlgo.addItem("")
        self.comboBoxAlgo.addItem("")


    def createChooseProperties(self):
        self.ChooseProperties = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.ChooseProperties.setFont(font)
        self.ChooseProperties.setTextFormat(Qt.PlainText)
        self.ChooseProperties.setAlignment(Qt.AlignCenter)


    def createPropertiesCheckboxes(self):
        self.CheckBoxDirected = QCheckBox(self.centralwidget)
        self.CheckBoxWeighted = QCheckBox(self.centralwidget)


    def createMenuBar(self):
        self.widget = QWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menuGraph = QMenu(self.menubar)
        self.actionOpen = QAction(self)
        self.actionSave = QAction(self)
        self.actionExit = QAction(self)

        self.setMenuBar(self.menubar)
        self.menuGraph.addAction(self.actionOpen)
        self.menuGraph.addAction(self.actionSave)
        self.menuGraph.addAction(self.actionExit)
        self.menubar.addAction(self.menuGraph.menuAction())


    def createCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)



    def setObjectsNames(self):
        self.setObjectName("MainWindow")
        self.centralwidget.setObjectName("centralwidget")
        self.widget.setObjectName("widget")
        self.menubar.setObjectName("menubar")
        self.menuGraph.setObjectName("menuGraph")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave.setObjectName("actionSave")
        self.graphwidget.setObjectName("graphwidget")
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.ChooseInputType.setObjectName("Choose input type")
        self.comboBoxInputType.setObjectName("Combo Box Input Type")
        self.ChooseAlgoritmnLabel.setObjectName("ChooseAlgoLabel")
        self.comboBoxAlgo.setObjectName("Combo Box Algo")
        self.ChooseProperties.setObjectName("ChooseProperties")
        self.CheckBoxDirected.setObjectName("CheckBoxDirected")
        self.CheckBoxWeighted.setObjectName("CheckBoxWeighted")
        self.TextMinPathStart.setObjectName("TextMinPathStart")
        self.TextMinPathGoal.setObjectName("TextMinPathStart")
        self.AlgoOutput.setObjectName("lgoOutput")



    def setGeometry(self):
        self.centralwidget.setGeometry(0, 0, 900, 600)
        self.widget.setGeometry(QRect(150, 110, 750, 450))
        self.menubar.setGeometry(QRect(0, 0, 904, 21))
        self.graphwidget.setGeometry(140, 15, 760, 590)
        self.horizontalLayoutWidget.setGeometry(QRect(5, 0, 140, 100))
        self.ChooseInputType.setGeometry(QRect(0, 120, 150, 30))
        self.comboBoxInputType.setGeometry(QRect(5, 155, 140, 30))
        self.ChooseAlgoritmnLabel.setGeometry(QRect(0, 200, 140, 30))
        self.comboBoxAlgo.setGeometry(QRect(5, 235, 140, 30))
        self.ChooseProperties.setGeometry(QRect(0, 280, 145, 30))
        self.CheckBoxDirected.setGeometry(QRect(5, 310, 91, 21))
        self.CheckBoxWeighted.setGeometry(QRect(5, 330, 91, 21))
        self.TextMinPathStart.setGeometry(QRect(15, 370, 50, 30))
        self.TextMinPathGoal.setGeometry(QRect(85, 370, 50, 30))
        self.AlgoOutput.setGeometry(35, 410, 80, 30)




    def setText(self):
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

        self.menuGraph.setTitle("File")
        self.actionOpen.setText("Import")
        self.actionSave.setText("Export")
        self.actionExit.setText("Exit")


    def getPathFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Graph Application", path.join(getcwd(), "input.txt"), options=options)
        if fileName:
            return fileName


    def touch(self, path):
        with open(path, "a"):
            utime(path, None)


    def createNewFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Graph Application", options=options)

        if fileName:
            pre, ext = path.splitext(fileName)
            fileName = pre + ".json"
            self.touch(fileName)
            return fileName


    def minPathTakeInput(self):
        v1, ok = QInputDialog.getInt(self, 'Input dialog', 'Enter your start vertice:')
        if not ok:
            return "Doesn't exist vertice"
        v2, ok = QInputDialog.getInt(self, 'Input dialog', 'Enter your end vertice:')
        if not ok:
            return "Doesn't exist vertice"
        return v1, v2


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
        if error == "Path error":
            msg.setWindowTitle("Path error")
            msg.setText("Choose correct file.")
        elif error == "File not match input type":
            msg.setWindowTitle("File not match input type")
            msg.setText("Choose file with correct graph input type.")
        elif error == "Vertices not in graph":
            msg.setWindowTitle("Vertices not in graph")
            msg.setText("Select vertices in graph ")
        elif error == "Minimal path error":
            msg.setWindowTitle("The path between the vertices does not exist ")
            msg.setText("Choose other vertices")
        elif error == "File corrupted":
            msg.setWindowTitle("File corrupted")
            msg.setText("Fix file or choose another")
        elif error == "Doesn't exist vertice":
            msg.setWindowTitle("Doesn't exist vertice")
            msg.setText("Input correct vertice")
        elif error == "Uncorrect weights":
            msg.setWindowTitle("Uncorrect weights")
            msg.setText("Weights need be natural")
        elif error == "Uncorrect vertice":
            msg.setWindowTitle("Uncorrect vertice")
            msg.setText("Vertice need be bigger than 0")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()