class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        i, j, res = 0, len(costs) - 1, 0
        while i < j:
            if costs[i][0] + costs[j][1] < costs[i][1] + costs[j][0]: res += costs[i][0] + costs[j][1]
            else: res += costs[i][1] + costs[j][0]
            i += 1
            j -= 1
        
        return res