class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.recursive(word1, word2, len(word1) - 1, len(word2) - 1)

        # dp = [[math.inf for j in range(len(word2))] for i in range(len(word1))]
        # return self.topDown(word1, word2, len(word1) - 1, len(word2) - 1, dp)

        return self.bottomUp(word1, word2)
    
    def recursive(self, word1, word2, index1, index2):
        if index1 < 0 and index2 < 0: return 0
        if index1 < 0: return index2 + 1
        if index2 < 0: return index1 + 1

        res, res1, res2, res3 = math.inf, math.inf, math.inf, math.inf
        if word1[index1] == word2[index2]: res = self.recursive(word1, word2, index1 - 1, index2 - 1)
        else:
            res1 = 1 + self.recursive(word1, word2, index1 - 1, index2 - 1)
            res2 = 1 + self.recursive(word1, word2, index1 - 1, index2)
            res3 = 1 + self.recursive(word1, word2, index1, index2 - 1)
        
        return min(res, res1, res2, res3)
    
    def topDown(self, word1, word2, index1, index2, dp):
        if index1 < 0 and index2 < 0: return 0
        if index1 < 0: return index2 + 1
        if index2 < 0: return index1 + 1

        res, res1, res2, res3 = math.inf, math.inf, math.inf, math.inf
        if word1[index1] == word2[index2]:
            if dp[index1][index2] == math.inf: 
                res = self.topDown(word1, word2, index1 - 1, index2 - 1, dp)
                dp[index1][index2] = min(dp[index1][index2], res)
        else:
            if dp[index1][index2] == math.inf:
                res1 = 1 + self.topDown(word1, word2, index1 - 1, index2 - 1, dp)
                res2 = 1 + self.topDown(word1, word2, index1 - 1, index2, dp)
                res3 = 1 + self.topDown(word1, word2, index1, index2 - 1, dp)

                dp[index1][index2] = min(dp[index1][index2], res1, res2, res3)

        return dp[index1][index2]

    def bottomUp(self, word1, word2):
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)

        dp = [[math.inf for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1): dp[i][0] = i
        for j in range(len(word2) + 1): dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
                else:
                    res1 = 1 + dp[i - 1][j - 1]
                    res2 = 1 + dp[i - 1][j]
                    res3 = 1 + dp[i][j - 1]
                    dp[i][j] = min(res1, res2, res3)

        return dp[len(word1)][len(word2)]