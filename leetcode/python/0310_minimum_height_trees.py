class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 and len(edges) == 0: return [0]

        inEdges = defaultdict(int)
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            inEdges[v] += 1
            inEdges[u] += 1

        leaves = deque()
        for v in adjList:
            if inEdges[v] == 1: leaves.append(v)
        
        # there cannot exist more than 2 centroids, we are trying to return the centroids and removing any leaves one by one up to the 2 centroids
        while n > 2:
            levelLength = len(leaves)
            n -= levelLength
            for i in range(levelLength):
                v = leaves.popleft()
                for child in adjList[v]:
                    inEdges[child] -= 1
                    if inEdges[child] == 1: leaves.append(child)
        
        return list(leaves)