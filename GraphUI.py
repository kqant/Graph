
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

class GraphUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph Application")
        self.setFixedSize(300, 300)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplayResult()
        self._createDisplayExpression()
        self._createButtons()

    def _createDisplayResult(self):
        self.displayResult = QLineEdit()
        self.displayResult.setFixedHeight(35)
        self.displayResult.setAlignment(Qt.Alignment.AlignCenter)
        self.displayResult.setReadOnly(True)
        self.displayResult.setText("Result")
        self.generalLayout.addWidget(self.displayResult)

    def _createDisplayExpression(self):
        self.displayExpression = QLineEdit()
        self.displayExpression.setFixedHeight(35)
        self.displayExpression.setAlignment(Qt.Alignment.AlignCenter)
        self.displayExpression.setText("Enter expression")
        self.generalLayout.addWidget(self.displayExpression)

    def _createButtons(self):
        self.buttons = {}
        buttons = {
            "DAROVA": (0, 0),
        }
        buttonsLayout = QGridLayout()
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayResultText(self, text):
        self.displayResult.setText(text)

    def displayExpressionText(self):
        return self.displayExpression.text()

