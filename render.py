
import networkx as nx


#Граф взят из примера input.png
def initTestGraphX():
    g = nx.Graph()
    g.add_nodes_from( [1, 2, 3] )
    g.add_edges_from( [ (1, 2), (2, 3), (3, 1) ] )
    return g

graph_test = initTestGraphX()


def drawGraph(view, graph=graph_test):
    pass



if __name__ == "__main__":
    pass

