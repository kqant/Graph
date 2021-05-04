
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

