"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None
        if node.neighbors == None: return Node(node.val, [])

        self.clones = {}
        # return self.dfs(node)
        return self.bfs(node)
    
    def bfs(self, node):
        queue = deque([node])
        self.clones[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in self.clones:
                    self.clones[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                self.clones[n].neighbors.append(self.clones[neighbor])
        
        return self.clones[node]
    
    def dfs(self, node):
        if node == None: return None
        if node in self.clones: return self.clones[node]

        clone = Node(node.val, [])
        self.clones[node] = clone

        for i in range(len(node.neighbors)): clone.neighbors.append(self.dfs(node.neighbors[i]))
        
        return clone