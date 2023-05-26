class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def recur(i):

            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i not in memo:
                memo[i] = recur(i-1) + recur(i-2) + recur(i-3)
                return memo[i]
            return memo[i]
        
        return recur(n)