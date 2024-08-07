class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    # dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
    # return self.knapsackRecursive(dp, profits, weights, capacity, 0)

    # return self.knapsackBottomUp(profits, weights, capacity)
    return self.knapsackBottomUpLinearSpace(profits, weights, capacity)
  
  def knapsackRecursive(self, dp, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits): return 0
    if dp[index][capacity] != -1: return dp[index][capacity]

    profit1 = 0
    if capacity - weights[index] >= 0: profit1 = profits[index] + self.knapsackRecursive(dp, profits, weights, capacity - weights[index], index + 1)
    profit2 = self.knapsackRecursive(dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]
  
  def knapsackBottomUp(self, profits, weights, capacity):
    if capacity <= 0 or len(profits) != len(weights) or len(profits) == 0: return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]

    for i in range(len(profits)): dp[i][0] = 0
    for c in range(capacity + 1):
      if c >= weights[0]: dp[0][c] = profits[0]
    
    for i in range(1, len(profits)):
      for c in range(1, capacity + 1):
        profit1, profit2 = 0, 0

        if c - weights[i] >= 0: profit1 = profits[i] + dp[i - 1][c - weights[i]]
        profit2 = dp[i - 1][c]

        dp[i][c] = max(profit1, profit2)
    
    return dp[len(profits) - 1][capacity]

  def knapsackBottomUpLinearSpace(self, profits, weights, capacity):
    if capacity <= 0 or len(profits) != len(weights) or len(profits) == 0: return 0

    dp = [0 for _ in range(capacity + 1)]

    for c in range(capacity + 1):
      if c >= weights[0]: dp[c] = profits[0]
    
    for i in range(1, len(profits)):
      for c in range(capacity, -1, -1):
        profit1, profit2 = 0, 0

        if c >= weights[i]: profit1 = profits[i] + dp[c - weights[i]]
        profit2 = dp[c]

        dp[c] = max(profit1, profit2)
    
    return dp[capacity]