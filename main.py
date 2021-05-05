from PyQt5.QtWidgets import QApplication

import sys

from bin.gui import Gag
from bin.graphCtrl import GraphCtrl
from bin.graphModel import GraphModel

from bin.input import *
from bin.render import *
from bin.algorithms import *



def main():
	app = QApplication(sys.argv)
	
	view = Gag()
	
	model = GraphModel()
	GraphCtrl(model, view)

	view.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
