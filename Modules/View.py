
"""
Модуль представления (View) отвечает за отображение данных
модели (Model) пользователя, реагируя на изменение модели (Model)
с помощью фреймворка PyQt5.
"""



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from Modules.Authors import getAuthors

from os import path, getcwd
## Абсолютный путь до иконки программы
iconPath = path.join(getcwd(), "Icons/GraphDrawer.svg")


class GraphUI(QMainWindow):
    """
    Класс представления (View) унаследованный от QMainWindow.

    Attributes:
        centralwidget (QWidget): Вентральный виджет.
        horizontalLayoutWidget (QWidget): Виджет горизонтального слоя.
        buttonsLayout (QHBoxLayout): Воризонтальный слой кнопок.
        graphwidget (QWidget): Виджет графа.
        generalLayout (QVBoxLayout): Главный вертикальный виджет.
        buttons (dict): Список кнопок.
        aboutButton (QPushButton): Виджет кнопки "About".
        figure (plt): Фигура matplotlib.
        canvas (FigureCanvas): Виджет холста.
        toolbar (NavigationToolbar): Виджет тулбара.
        TextMinPathStart (QLineEdit): Виджет поля "Start".
        TextMinPathGoal (QLineEdit): Виджет поля "Goal".
        AlgoOutput (QLineEdit): Виджет поля результата алгоритма.
    """
    def __init__(self, parent = None):
        super(GraphUI, self).__init__(parent)
        self.setWindowTitle("GraphDrawer")
        self.setFixedSize(900, 615)
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
        self._createAboutButton()
        self._createCanvas()
        self._createMinPathInput()
        self._createAlgoOutput()

        self.statusBar().showMessage("Choose input file")

        QMetaObject.connectSlotsByName(self)

        self._setObjectsNames()
        self._setGeometry()
        self.figure.clf()


    def _createButtons(self):
        """Создание кнопок."""
        self.buttons = {}
        buttons = {
            "Input File": (0, 5, 105, 30),
            "⭯": (0, 70, 30, 30),
            "Clear": (30, 5, 140, 30),
            "Coloring": (45, 5, 140, 45),
            "Min Path": (50, 5, 140, 45)
        }
        buttonsLayout = QGridLayout()
        for btnText, prop in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(prop[2], prop[3])
            font = QFont()
            if btnText == "⭯":
                font.setPointSize(18)
                self.buttons[btnText].setDisabled(True)
            else:
                font.setPointSize(12)
            self.buttons[btnText].setFont(font)
            buttonsLayout.addWidget(self.buttons[btnText], prop[0], prop[1])
        self.buttonsLayout.addLayout(buttonsLayout)


    def _createAboutButton(self):
        """Создание кнопки "About"."""
        self.aboutButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(12)
        self.aboutButton.setFont(font)
        self.aboutButton.setText("About")


    def _createCanvas(self):
        """Создание холста."""
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.generalLayout.addWidget(self.toolbar)
        self.generalLayout.addWidget(self.canvas)


    def _createMinPathInput(self):
        """Создание поля с выводом результата алгоритма."""
        self.TextMinPathStart = QLineEdit(self.centralwidget)
        self.TextMinPathGoal = QLineEdit(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.TextMinPathStart.setFont(font)
        self.TextMinPathGoal.setFont(font)
        self.TextMinPathStart.setAlignment(Qt.AlignHCenter)
        self.TextMinPathGoal.setAlignment(Qt.AlignHCenter)
        self.TextMinPathStart.setPlaceholderText("Start")
        self.TextMinPathGoal.setPlaceholderText("Goal")


    def _createAlgoOutput(self):
        """Создание поля с выводом результата алгоритма."""
        self.AlgoOutput = QLineEdit(self.centralwidget)
        font = QFont()
        font.setPointSize(11)
        self.AlgoOutput.setFont(font)
        self.AlgoOutput.setReadOnly(True)
        self.AlgoOutput.setAlignment(Qt.AlignHCenter)
        self.AlgoOutput.setText("Algorithm result")


    def _setObjectsNames(self):
        """Установка имён объектов."""
        self.setObjectName("MainWindow")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.graphwidget.setObjectName("graphwidget")
        self.TextMinPathStart.setObjectName("TextMinPathStart")
        self.TextMinPathGoal.setObjectName("TextMinPathStart")
        self.AlgoOutput.setObjectName("AlgoOutput")


    def _setGeometry(self):
        """Установка геометрии объектов."""
        self.centralwidget.setGeometry(0, 0, 900, 600)
        self.horizontalLayoutWidget.setGeometry(QRect(5, 10, 140, 170))
        self.graphwidget.setGeometry(140, 0, 760, 610)
        self.aboutButton.setGeometry(35, 230, 80, 30)
        self.TextMinPathStart.setGeometry(QRect(5, 180, 68, 30))
        self.TextMinPathGoal.setGeometry(QRect(76, 180, 68, 30))
        self.AlgoOutput.setGeometry(5, 565, 140, 30)


    def getPathFile(self):
        """
        Получение пути из диалогового окна выбора файла.

        Returns:
            string: Абсолютный путь до файла.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Graph Application", getcwd(),
                                                  "Graph files (*.list *.mat *.listw *.listwd *.listd *.matw *.matd *.matwd)", options=options)
        if fileName:
            return fileName


    def showError(self, error):
        """
        Вывод сообщения об ошибке.

        Args:
            error (string): Cтрока с ошибкой.
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setWindowTitle("Error")
        msg.setText(str(error))

        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


    def aboutAuthors(self):
        """Вывод сообщения об авторах из модуля Authors."""
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)

        mb.setWindowTitle("Authors")
        mb.setText(getAuthors())

        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec()

 