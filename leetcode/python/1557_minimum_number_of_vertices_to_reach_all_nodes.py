class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_nodes = set()
        for u, v in edges: incoming_nodes.add(v)
        
        res = []
        for i in range(n):
            if i not in incoming_nodes: res.append(i)
        
        return res