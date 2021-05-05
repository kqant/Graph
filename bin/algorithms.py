from random import random


def drawGraph(graph):
    pass


def drawGraph(view):
    view.figure.clf()
    data = [random() for i in range(10)]
    ax = view.figure.add_subplot(111)
    ax.clear()
    ax.plot(data, '*-')
    view.canvas.draw()


if __name__ == "__main__":
    pass
