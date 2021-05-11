from os import path, getcwd
from random import randint
from PyQt5.QtWidgets import QMessageBox
from collections import deque
import json



class MyDecoder(json.JSONDecoder):
    def decode(self, z):
        result = super().decode(z)
        return self._decode(result)

    def _decode(self, z):
        if isinstance(z, str):
            try:
                return int(z)
            except ValueError:
                return z
        elif isinstance(z, dict):
            return {self._decode(k): self._decode(v) for k, v in z.items()}
        elif isinstance(z, list):
            return [self._decode(v) for v in z]
        else:
            return z


class Graph:
    adj: dict
    directed: bool
    weighted: bool
    filePath: str
    inputType: str
    algoValues: dict


    def __init__(self):
        self.adj = {}
        self.directed = False
        self.weighted = False
        self.filePath = None
        self.inputType ="Adjacency List"
        self.algoValues = {}

    def getFields(self):
        return self.adj, self.directed, self.weighted, self.algoValues


    def print(self):
        for key, value in self.adj.items():
            print(f"[{key}] -> ", end="")
            print(f"{value}")


    def addVertices(self, *verts):
        for v in verts:
            if v not in self.adj.keys():
                self.adj[v] = {}


    def addEdges(self, start, ends):
        self.addVertices(*range(1, max(start, *ends)+1))
        self.adj[start] = {**self.adj[start], **ends}
        if not self.directed:
            for end in ends.keys():
                if end in self.adj.keys():
                    self.adj[end] = {**self.adj[end], **{start: ends[end]}}
                else:
                    self.adj[end] = {start: ends[end]}


    def convert_matrix_to_list(self, matrix):
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


    def importGraph(self, path):
        try:
            with open(path, "r") as file:
                aFile = json.load(file, cls=MyDecoder)
                self.adj = aFile['adj']
                self.directed = aFile['directed']
                self.weighted = aFile['weighted']
                self.algoValues = aFile['algoValues']
        except Exception:
            return "File corrupted"


    def exportGraph(self, path):
        with open(path, "w") as file:
            toSaveDict = {}
            toSaveDict["adj"] = self.adj
            toSaveDict["directed"] = self.directed
            toSaveDict["weighted"] = self.weighted
            toSaveDict["algoValues"] = self.algoValues
            json.dump(toSaveDict, fp=file, sort_keys=True, indent=4)


    def readGraph(self):
        try:
            with open(self.filePath, "r") as fin:
                if self.inputType == "Adjacency List":
                    self.adj = {}
                    while True:
                        temp = [int(i) for i in fin.readline().split()]
                        if temp == []:
                            break
                        if self.weighted:
                            for i in range(0, len(temp), 3):
                                if temp[i+2] < 0:
                                    print("negative weights?")
                                    self._adj = {}
                                    return "negative weights?"
                                self.addEdges(temp[i], {temp[i+1]:temp[i+2]})
                        else:
                            for i in range(0, len(temp), 2):
                                self.addEdges(temp[i], {temp[i+1]:1})
                    self.addVertices(max(self.adj.keys()))
                elif self.inputType == "Adjacency Matrix":
                    matrix = []
                    while True:
                        temp = [int(i) for i in fin.readline().split()]
                        if temp == []:
                            break
                        matrix.append(temp)
                    self.adj = self.convert_matrix_to_list(matrix)
        except (FileNotFoundError, TypeError):
            self.adj = {}
            print("Path error")
            return "Path error"
        except (IndexError, ValueError):
            self.adj = {}
            print("File not match input type")
            return "File not match input type"


    def minPathFind(self, start, goal):
        graph = self.adj
        if start not in graph or goal not in graph:
            print("Vertices not in graph")
            return "Vertices not in graph"
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
            print("Minimal path error")
            return "Minimal path error"


    def coloring(self):
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
            if colored[v] == None:
                colored[v] = cl
                smList.append(v)
                for j in vertList:
                    j = j[0]
                    if colored[j] == None:
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
        return res


    def initGraphFile(self, filepath):
        self.filePath = filepath
        