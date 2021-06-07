
from random import randint
from collections import deque
from os.path import splitext



class Graph:
    adj: dict
    directed: bool
    weighted: bool
    filePath: str
    funcRead: dict

    def __init__(self):
        self.adj = {}
        self.directed = False
        self.weighted = False
        self.filePath = ""
        self.funcRead = {
            ".list": (".list", False, False,),
            ".mat": (".mat", False, False),
            ".listw": (".list", True, False),
            ".listd": (".list", False, True),
            ".listwd": ('.list', True, True),
            ".listdw": ('.list', True, True),
            ".matw": (".mat", True, False),
            ".matd": (".mat", False, True),
            ".matdw": (".mat", True, True),
            ".matwd": (".mat", True, True)
        }


    def _addVertices(self, *verts):
        for v in verts:
            if v not in self.adj.keys():
                self.adj[v] = {}


    def _addEdges(self, start, ends):
        self._addVertices(*range(1, max(start, *ends)+1))
        self.adj[start] = {**self.adj[start], **ends}
        if not self.directed:
            for end in ends.keys():
                if end in self.adj.keys():
                    self.adj[end] = {**self.adj[end], **{start: ends[end]}}
                else:
                    self.adj[end] = {start: ends[end]}


    def _matrixToList(self, matrix):
        G = {}
        for a in range(len(matrix)):
            if matrix[a].count(0) != len(matrix):
                for b in range(len(matrix)):
                    if matrix[a][b]:
                        if a + 1 not in G:
                            G[a + 1] = {b + 1: matrix[a][b]}
                        else:
                            G[a + 1][b + 1] = matrix[a][b]
            else:
                G[a + 1] = set()
        return G


    def _readList(self):
        with open(self.filePath, "r") as fin:
            while True:
                temp = [int(i) for i in fin.readline().split()]
                if temp == []:
                    break
                if self.weighted:
                    for i in range(0, len(temp), 3):
                        if temp[i] <= 0 or temp[i+1] <= 0:
                            self._adj = {}
                            raise Exception("Uncorrect vertice")
                        elif temp[i+2] <= 0:
                            self._adj = {}
                            raise Exception("Uncorrect weights")
                        self._addEdges(temp[i], {temp[i+1]:temp[i+2]})
                else:
                    for i in range(0, len(temp), 2):
                        if temp[i] <= 0 or temp[i+1] <= 0:
                            print("Uncorrect vertice")
                            self._adj = {}
                            return "Uncorrect vertice"
                        self._addEdges(temp[i], {temp[i+1]:1})
            self._addVertices(max(self.adj.keys()))


    def _readMatrix(self):
        with open(self.filePath, "r") as fin:
            matrix = []
            while True:
                if self.weighted:
                    temp = [int(i) for i in fin.readline().split()]
                else:
                    temp = [1 if int(i) else 0 for i in fin.readline().split()]
                if temp == []:
                    break
                matrix.append(temp)
            self.adj = self._matrixToList(matrix)


    def clearGraph(self):
        self.adj = {}
        self.directed = False
        self.weighted = False
        self.filePath = ""


    def getFields(self):
        return self.adj, self.directed, self.weighted


    def initGraphFile(self, filepath):
        self.filePath = filepath


    def readGraph(self):
        self.adj = {}
        try:
            file_ext = splitext(self.filePath)[1]
        except TypeError:
            raise Exception("Choose file first!")

        try:
            ex,w,d = self.funcRead[file_ext]
            self.weighted = w
            self.directed = d
            if ex == '.list':
                self._readList()
            elif ex == '.mat':
                self._readMatrix()
        except KeyError:
            raise Exception(f"Incorrect file type: {file_ext}")
        except (FileNotFoundError, TypeError):
            raise Exception("Path Error")
        except (IndexError, ValueError):
            raise Exception("File not match input type")


    def minPathFind(self, start, goal):
        if not self.adj:
            raise Exception("Graph is empty")
        if not self.weighted:
            raise Exception("Graph not weighted")

        graph = self.adj

        try:
            start, goal = int(start), int(goal)
        except Exception:
            raise Exception("Unknown vertices")
        if start not in graph or goal not in graph:
            raise Exception("Vertices not in graph")

        queue = deque()
        visited = {start: 0}
        tmpPath = {}
        queue.append(start)
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if u not in visited or visited[v] + graph[v][u] < visited[u]:
                    visited[u] = visited[v] + graph[v][u]
                    queue.append(u)
                    tmpPath[u] = v
        v = goal
        path = deque()
        path.append(v)
        if v in tmpPath:
            while v != start:
                v = tmpPath[v]
                path.appendleft(v)
            return visited[goal], list(path)
        elif start == goal:
            return 0, [start]
        else:
            raise Exception("Path not found")


    def coloring(self):
        if not self.adj:
            raise Exception("Graph is empty")
        graph = self.adj
        tmp = {x: 0 for x in graph}
        for x in graph:
            if graph[x]:
                tmp[x] = len(graph[x].keys())
            else:
                tmp[x] = 0
        vertList = list(tmp.items())
        vertList.sort(key=lambda i: i[1])
        colored = {x: None for x in graph}
        flag = True
        cl = 0
        smList = []
        for v in vertList:
            v = v[0]
            if colored[v] is None:
                colored[v] = cl
                smList.append(v)
                for j in vertList:
                    j = j[0]
                    if colored[j] is None:
                        for sm in smList:
                            if sm in graph[j] or j in graph[sm] and flag:
                                flag = False
                        if flag:
                            colored[j] = cl
                            smList.append(j)
                        flag = True
                smList = []
                cl += 1
        res = {}
        existColors = {}
        for i in colored:
            if colored[i] in existColors.keys():
                res[i] = existColors[colored[i]]
            else:
                existColors[colored[i]] = (randint(0, 255), randint(0, 255),randint(0, 255))
                res[i] = existColors[colored[i]]
        return cl, res

