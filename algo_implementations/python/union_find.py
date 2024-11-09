class UnionFind:
  def __init__(self):
    self.parent = []
  
  def find(self, i):
    if self.parent[i] == i: return i
    return self.find(self.parent[i])
  
  def union(self, i, j):
    iRep = self.find(i)
    jRep = self.find(j)
    
    if iRep == jRep: return
    
    self.parent[iRep] = jRep

class UnionFindOptimized:
  def __init__(self, n):
    self.rank = [1 for _ in range(n)]
    self.parent = [i for i in range(n)]
  
  def find(self, x):
    if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    xSet = self.find(x)
    ySet = self.find(y)
    
    if xSet == ySet: return
    
    if self.rank[xSet] < self.rank[ySet]: self.parent[xSet] = ySet
    elif self.rank[xSet] > self.rank[ySet]: self.parent[ySet] = xSet
    else:
      self.parent[ySet] = xSet
      self.rank[xSet] += 1