from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt




class Ui_MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.setFixedSize(900, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setGeometry(0, 0, 900, 600)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 900, 100))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self._createButtons() # основные кнопки

        self.ChooseAlgoritmnLabel = QLabel(self.centralwidget)
        self.ChooseAlgoritmnLabel.setGeometry(QRect(20, 120, 150, 30))
        font = QFont()
        font.setPointSize(9)
        self.ChooseAlgoritmnLabel.setFont(font)
        self.ChooseAlgoritmnLabel.setFrameShape(QFrame.StyledPanel)
        self.ChooseAlgoritmnLabel.setTextFormat(Qt.PlainText)
        self.ChooseAlgoritmnLabel.setAlignment(Qt.AlignCenter)
        self.ChooseAlgoritmnLabel.setObjectName("ChooseAlgoLabel")


        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QRect(20, 160, 150, 30))
        self.comboBox.setObjectName("SomeOptions")  # изменить название обьекта с выпадающим списком
        font = QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.ChooseAlgoLabel_2 = QLabel(self.centralwidget)
        self.ChooseAlgoLabel_2.setGeometry(QRect(20, 200, 150, 30))
        font = QFont()
        font.setPointSize(9)
        self.ChooseAlgoLabel_2.setFont(font)
        self.ChooseAlgoLabel_2.setFrameShape(QFrame.StyledPanel)
        self.ChooseAlgoLabel_2.setTextFormat(Qt.PlainText)
        self.ChooseAlgoLabel_2.setAlignment(Qt.AlignCenter)
        self.ChooseAlgoLabel_2.setObjectName("ChooseAlgoLabel_2")


        self.CheckBoxDirected = QCheckBox(self.centralwidget)
        self.CheckBoxDirected.setGeometry(QRect(20, 240, 91, 21))
        self.CheckBoxDirected.setObjectName("CheckBoxDirected")


        self.CheckBoxWeighted = QCheckBox(self.centralwidget)
        self.CheckBoxWeighted.setGeometry(QRect(20, 260, 91, 21))
        self.CheckBoxWeighted.setObjectName("CheckBoxWeighted")


        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(150, 110, 750, 450))
        self.widget.setObjectName("widget")
        self.setCentralWidget(self.centralwidget)


        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")


        self.menuGraph = QMenu(self.menubar)
        self.menuGraph.setObjectName("menuGraph")
        self.setMenuBar(self.menubar)


        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)


        self.actionNew = QAction(self)
        self.actionNew.setObjectName("actionNew")


        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")


        self.actionSave = QAction(self)
        self.actionSave.setObjectName("actionSave")


        self.menuGraph.addAction(self.actionNew)
        self.menuGraph.addAction(self.actionOpen)
        self.menuGraph.addAction(self.actionSave)
        self.menubar.addAction(self.menuGraph.menuAction())


        self.grafwidget = QWidget(self)
        self.grafwidget.setGeometry(180, 130, 700, 450)
        self.grafwidget.setObjectName("grafwidget")


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)


        self.generalLayout = QVBoxLayout(self.grafwidget)
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)


        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)


        self.setLayout(self.generalLayout)


    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "Draw": (0, 0, 200, 100),
            "Read": (0, 1, 200, 100),
            "Algorithms": (0, 2, 200, 100),
            "Save": (0, 3, 200, 100),
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        self.horizontalLayout_2.addLayout(buttonsLayout)


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CheckBoxWeighted.setText(_translate("MainWindow", "Weighted"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Min Path Finding"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Coloring"))
        self.ChooseAlgoritmnLabel.setText(_translate("MainWindow", "Choose algorithm"))
        self.CheckBoxDirected.setText(_translate("MainWindow", "Directed"))
        self.ChooseAlgoLabel_2.setText(_translate("MainWindow", "Choose properties"))
        self.menuGraph.setTitle(_translate("MainWindow", "Graph"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


    def getPathFile(self):
        return QFileDialog.getOpenFileName()[0]


