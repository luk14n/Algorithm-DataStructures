import sys


class DSU:
    def __init__(self):
        self.previous = {}

    def set_make(self, v):
        self.previous[v] = v

    def set_find(self, v):
        if self.previous[v] == v: return v
        return self.set_find(self.previous[v])

    def set_union(self, v1, v2):
        v1_rep = self.set_find(v1)
        v2_rep = self.set_find(v2)
        if v1_rep != v2_rep:
            self.previous[v1_rep] = v2_rep


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def set_make(self, u, v, w):
        self.graph.append([u, v, w])

    def set_find(self, parent, i):
        if parent[i] == i:
            return i
        return self.set_find(parent, parent[i])

    def set_union(self, parent, rank, x, y):
        xroot = self.set_find(parent, x)
        yroot = self.set_find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def show_krus(self):
        for g in self.graph:
            print("%d -- %d == %d" % (g[0], g[1], g[2]))

    def Kruskal(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.set_find(parent, u)
            y = self.set_find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.set_union(parent, rank, x, y)
        minimumCost = 0
        print("Ребра Мінімального каркасу")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))

    def printMST(self, parent):
        print("Ребра Мінімального каркасу")
        for i in range(1, self.V):
            print(parent[i], "--", i, "==", self.adjMatrix[i][parent[i]])

    def minKey(self, key, mstSet):
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def createAdjMatrix(self):
        adjMatrix = []
        i = 0
        while i < self.V:
            adjMatrix.append([])
            j = 0
            while j < self.V:
                adjMatrix[i].append(0)
                j += 1
            i += 1
        i = 0
        while i < self.graph.__len__():
            adjMatrix[self.graph[i][0]][self.graph[i][1]] = self.graph[i][2]
            adjMatrix[self.graph[i][1]][self.graph[i][0]] = self.graph[i][2]
            i += 1
        return adjMatrix

    def primMST(self):
        self.adjMatrix = self.createAdjMatrix()
        key = [1000000] * self.V
        parent = [None] * self.V  #
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.adjMatrix[u][v] > 0 and mstSet[v] == False and key[v] > self.adjMatrix[u][v]:
                    key[v] = self.adjMatrix[u][v]
                    parent[v] = u
        self.printMST(parent)
