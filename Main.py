
"""Главный модуль программы."""



from sys import argv, exit

from PyQt5.QtWidgets import QApplication

from Modules.View import GraphUI
from Modules.Model import GraphModel
from Modules.Control import GraphCtrl


def main():
	"""Точка входа программы."""
	app = QApplication(argv)

	view = GraphUI()
	model = GraphModel()
	GraphCtrl(view, model)

	view.show()
	exit(app.exec())

if __name__ == "__main__":
	main()

