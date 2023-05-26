class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n =  len(cost)
        if n == 2:
            return min(cost)
        cost.append(0)

        def recur(i):
            if i >= n - 1:
                return cost[i]
            
            if i not in memo:
                memo[i] = cost[i] + min(recur(i+1) ,recur(i+2))
                return memo[i]

            return memo[i]
        recur(0)
        return min(memo[1] ,memo[0])
