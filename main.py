<<<<<<< Updated upstream

import sys

from PyQt6.QtWidgets import QApplication

from GraphUI import GraphUI
from GraphModel import GraphModel
from GraphCtrl import GraphCtrl


def main():
    app = QApplication(sys.argv)

    #init view
    view = GraphUI()
    view.show()

    #init model
    model = GraphModel()

    #init control
    GraphCtrl(model, view)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

=======
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
>>>>>>> Stashed changes
