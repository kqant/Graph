
import networkx as nx



def drawDefault(view, adj, isDir, weighted):
    view.figure.clf()
    
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    for i in adj:
        G.add_node(i)

    if (weighted):
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j, weight=adj[i][j])
    else:
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j)

    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color='#750000')

    view.canvas.draw()


def drawMinPath(view, adj, isDir, weighted, path):
    view.figure.clf()
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    for i in adj:
        G.add_node(i)
    
    for i in adj:
        for j in adj[i]:
            if (weighted):
                G.add_edge(i, j, weight=adj[i][j], color='#750000')
            else:
                G.add_edge(i, j, color='#750000')
            for k in range(len(path) - 1):
                if ((path[k] == i) and (path[k + 1] == j)) or ((path[k] == j) and (path[k+1] == i)):
                    if (weighted):
                        G.add_edge(i, j, weight=adj[i][j], color='blue')
                    else:
                        G.add_edge(i, j, color='blue')
                    break

    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color='#003473', font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color=nx.get_edge_attributes(G,'color').values())
    
    view.canvas.draw()


def drawColoring(view, adj, isDir, weighted, colors):
    view.figure.clf()
    if (isDir):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
        
    def converter(colors):
        col_converted = []
        for i in colors:
            col_converted.append((colors[i][0] / 255, colors[i][1] / 255, colors[i][2] / 255))
        return col_converted
    
    for i in adj:
        G.add_node(i)
    
    if (weighted):
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j, weight=adj[i][j])
    else:
        for i in adj:
            for j in adj[i]:
                G.add_edge(i, j)
    
    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos=pos, with_labels=True, node_color=converter(colors), font_color='white', font_weight='bold', alpha=0.9)
    nx.draw_networkx_edge_labels(G, pos=pos, font_color='black', font_weight=700,
                                edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_edges(G, pos=pos, width=1, edge_color='#750000')
    
    view.canvas.draw()


def chooseDrawType(graphctrl):
    algo = graphctrl.view.comboBoxAlgo.currentText()
    adj, isDir, weighted, algoValues = graphctrl.model.graph.getFields()
    
    if algo == "Default":
        drawDefault(graphctrl.view, adj, isDir, weighted)
    
    elif algo == "Min Path Finding":
        start, end = graphctrl.view.minPathTakeInput()
        if start == None:
            return
        length, path = graphctrl.model.graph.minPathFind(start, end, graphctrl.model.graph.adj)
        if length == None:
            return
        drawMinPath(graphctrl.view, adj, isDir, weighted, path)
    
    elif algo == "Coloring":
        colors = graphctrl.model.graph.coloring(adj)
        drawColoring(graphctrl.view, adj, isDir, weighted, colors)

