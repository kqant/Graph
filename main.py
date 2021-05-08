
import sys

from PyQt5.QtWidgets import QApplication

from View import GraphUI
from uiTest import Ui_MainWindow
from Model import GraphModel
from Control import GraphCtrl


def main():
	app = QApplication(sys.argv)

	view = Ui_MainWindow()
	view.show()

	model = GraphModel()

	GraphCtrl(model, view)
	
	sys.exit(app.exec())

if __name__ == "__main__":
	main()

