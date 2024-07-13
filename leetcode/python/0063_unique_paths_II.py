class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        # return self.bottomUpDP(obstacleGrid, dp)
        
        return self.bottomUpDPConstantSpace(obstacleGrid)
    
    def bottomUpDP(self, obstacleGrid, dp):
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1: continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
    
    def bottomUpDPConstantSpace(self, obstacleGrid):
        obstacle = False
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1 or obstacle:
                obstacleGrid[i][0] = 0
                obstacle = True
            else: obstacleGrid[i][0] = 1
        
        obstacle = True if obstacleGrid[0][0] == 0 else False
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1 or obstacle:
                obstacleGrid[0][i] = 0
                obstacle = True
            else: obstacleGrid[0][i] = 1
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        
        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]