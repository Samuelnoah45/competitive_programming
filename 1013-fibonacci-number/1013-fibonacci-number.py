class Solution:
    def fib(self, n: int) -> int:
        # memo = {}
        # if n < 2:
        #     return n
        # if n in memo:
        #     return memo[n]
        # memo[n] = self.fib(n-1) + self.fib(n-2)
        # return memo[n]
        dp = [0] * (n + 1)
        if n ==0:
            return 0 
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[n]
       
        