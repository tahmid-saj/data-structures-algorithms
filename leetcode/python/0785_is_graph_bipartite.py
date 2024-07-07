class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0 for i in range(n)]
    
    def find(self, i):
        if self.parent[i] != i: self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        iSet, jSet = self.find(i), self.find(j)
        if iSet == jSet: return

        if self.size[iSet] < self.size[jSet]: self.parent[iSet] = jSet
        elif self.size[iSet] > self.size[iSet]: self.parent[jSet] = iSet
        else:
            self.size[jSet] += 1
            self.parent[iSet] = jSet

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dsu = DSU(len(graph))

        for i in range(len(graph)):
            if len(graph[i]) > 0:
                parent = dsu.find(i)
                firstNeighbour = graph[i][0]
                for neighbour in graph[i]:
                    if parent == dsu.find(neighbour): return False
                    dsu.union(firstNeighbour, neighbour)
        
        return True