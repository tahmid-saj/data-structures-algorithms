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
        elif self.size[iSet] > self.size[jSet]: self.parent[jSet] = iSet
        else:
            self.size[jSet] += 1
            self.parent[iSet] = jSet

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)

        for u, v in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
            else: return [u, v]
        
        return [-1, -1]