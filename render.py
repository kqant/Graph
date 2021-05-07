
import networkx as nx


#Граф взят из примера input.png
def initTestGraphX():
    g = nx.Graph()
    g.add_nodes_from( [1, 2, 3] )
    g.add_edges_from( [ (1, 2), (2, 3), (3, 1) ] )
    return g

graph_test = {1:{3: 228}, 2:{4:12, 5: 512}}


def drawGraph(view, graph=graph_test, is_dir=1):
    view.figure.clf()

    if (is_dir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for i in graph_test:
        for j in graph_test[i]:
            G.add_edge(i, j, weight=graph_test[i][j])

    pos = nx.planar_layout(G)

    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=3, edge_color='#750000')

    view.canvas.draw()



if __name__ == "__main__":
    pass

