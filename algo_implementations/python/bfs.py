from collections import defaultdict, deque

class GraphUndirected:
  def __init__(self, vertices):
    self.vertices = vertices
    self.adjList = defaultdict(list)
  
  def addEdge(self, u, v):
    self.adjList[u].append(v)
    self.adjList[v].append(u)
  
  def bfs(self, start):
    visited = [False] * self.vertices
    queue = deque([start])
    visited[start] = True
    
    while queue:
      curr = queue.popleft()
      print(curr)
      
      for neighbor in self.adjList(curr):
        if not visited[neighbor]:
          queue.append(neighbor)
          visited[neighbor] = True