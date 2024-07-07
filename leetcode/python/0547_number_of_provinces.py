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

        if self.size[i] < self.size[j]: self.parent[iSet] = jSet
        elif self.size[i] > self.size[j]: self.parent[jSet] = iSet
        else:
            self.size[jSet] += 1
            self.parent[iSet] = jSet

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # provinces = 0
        # visited = set()
        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         # self.stack(isConnected, visited, i)
        #         self.dfs(isConnected, visited, i)
        #         provinces += 1
        
        # return provinces

        return self.unionFind(isConnected)

    def stack(self, isConnected, visited, city):
        stk = [city]
        visited.add(city)

        while stk:
            city = stk.pop()

            for j in range(len(isConnected[city])):
                if isConnected[city][j] == 1 and j != city and j not in visited:
                    visited.add(j)
                    stk.append(j)
    
    def dfs(self, isConnected, visited, i):
        visited.add(i)

        for j in range(len(isConnected[i])):
            if i != j and isConnected[i][j] == 1 and j not in visited:
                self.dfs(isConnected, visited, j)
    
    def unionFind(self, isConnected):
        provinces = len(isConnected)
        dsu = DSU(provinces + 1)

        for u in range(len(isConnected)):
            for v in range(len(isConnected[0])):
                if isConnected[u][v] == 1 and dsu.find(u) != dsu.find(v):
                    dsu.union(u, v)
                    provinces -= 1

        return provinces