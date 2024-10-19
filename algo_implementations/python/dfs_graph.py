class GraphUndirected:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adjList = [[] for _ in range(vertices)]
  
  def addEdge(self, u, v):
    self.adjList[u].append(v)
    self.adjList[v].append(u)
  
  def dfs(self, start):
    visited = [False] * self.vertices
    stack = []
    
    stack.append(start)
    visited[start] = True
    
    while stack:
      curr = stack.pop()
      print(curr)
      
      for neighbor in self.adjList[curr]:
        if not visited[neighbor]:
          stack.append(neighbor)
          visited[neighbor] = True