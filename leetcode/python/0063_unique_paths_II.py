class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        # return self.bottomUpDP(obstacleGrid, dp)
        
        return self.bottomUpDPConstantSpace(obstacleGrid)
    
    def bottomUpDP(self, grid, dp):
        for i in range(len(grid)): 
            if grid[i][0] != 1: dp[i][0] = 1
            else: break
        
        for j in range(len(grid[0])):
            if grid[0][j] != 1: dp[0][j] = 1
            else: break
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] != 1: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else: dp[i][j] = 0
        
        return dp[len(grid) - 1][len(grid[0]) - 1]
    
    def bottomUpDPConstantSpace(self, grid):
        prev = [0 for _ in range(len(grid[0]))]

        for j in range(len(grid[0])):
            if grid[0][j] != 1: prev[j] = 1
            else: break
        
        obstacle = False
        for i in range(1, len(grid)):
            curr = [0 for _ in range(len(grid[0]))]
            if grid[i][0] == 1 or prev[0] == 0: obstacle = True
            if not obstacle: curr[0] = 1
            for j in range(1, len(grid[0])):
                if grid[i][j] != 1: curr[j] = prev[j] + curr[j - 1]
                else: curr[j] = 0
            prev = curr

        return prev[len(grid[0]) - 1]