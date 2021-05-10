
import networkx as nx



def drawDefault(view, adj, is_dir, weighted):
    view.figure.clf()
    
    if (is_dir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    for i in adj:
        for j in adj[i]:
            G.add_edge(i, j, weight=adj[i][j])

    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=2, edge_color='#750000')

    view.canvas.draw()


def drawMinPath(view, adj, is_dir, weighted, path):
    view.figure.clf()
    
    if (is_dir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    for i in adj:
        for j in adj[i]:
            G.add_edge(i, j, weight=adj[i][j], color='#750000')
            for k in range(len(path) - 1):
                if ((path[k] == i) and (path[k + 1] == j)) or ((path[k] == j) and (path[k+1] == i)):
                    G.add_edge(i, j, weight=adj[i][j], color='blue')
                    break

    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=2, edge_color=nx.get_edge_attributes(G,'color').values())
    
    view.canvas.draw()


def drawColoring(view, adj, is_dir, weighted, colors):
    view.figure.clf()
    print(colors)
    if (is_dir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    def converter(colors):
        col_converted = []
        for i in colors:
            col_converted.append((colors[i][0] / 255, colors[i][1] / 255, colors[i][2] / 255))
        return col_converted
    
    for i in adj:
        for j in adj[i]:
            G.add_edge(i, j, weight=adj[i][j], color='#750000')
    
    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color=converter(colors), font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=2, edge_color='#750000')
    
    view.canvas.draw()


def chooseDrawType(graphctrl):
    algo = graphctrl._view.comboBoxAlgo.currentText()
    adj, is_dir, weighted, algoValues = graphctrl._model.graph.getFields()
    
    if algo == "Default":
        drawDefault(graphctrl._view, adj, is_dir, weighted)
    
    elif algo == "Min Path Finding":
        start, end = graphctrl._view.minPathTakeInput()
        length, path = graphctrl._model.graph.minPathFind(start, end, graphctrl._model.graph._adj)
        drawMinPath(graphctrl._view, adj, is_dir, weighted, path)
    
    elif algo == "Coloring":
        colors = graphctrl._model.graph.coloring(adj)
        drawColoring(graphctrl._view, adj, is_dir, weighted, colors)

