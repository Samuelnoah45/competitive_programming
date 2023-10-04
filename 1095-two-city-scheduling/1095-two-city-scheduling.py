class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs = sorted(costs, key=lambda x: x[0] - x[1])

        minCost, count, n = 0, 0, len(costs)

        for i in range(n):
            if i < n / 2:
                minCost += costs[i][0]
            else:
                minCost += costs[i][1]
        
        return minCost