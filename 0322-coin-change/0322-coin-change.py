class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_depth = float('inf')
        memo = {}
        def dfs(x):
            tt = float('inf')
            if x == 0:
                return 0
            if x < 0:
                return float('inf')
            if x in memo:
                return memo[x]

            for i in range(len(coins)):
                tt = min(tt, dfs(x - coins[i]))
            memo[x] = tt + 1
            return tt + 1

        min_depth = dfs(amount)

        return min_depth if min_depth != float('inf') else -1