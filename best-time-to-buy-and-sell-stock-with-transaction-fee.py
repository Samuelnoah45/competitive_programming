class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        stocks = [True, False]
        dp = [[0]*(len(prices)+1) for _ in range(2)]

        for idx in range(len(prices)-1 ,-1 ,-1):
            for stock in stocks:
                if stock:
                    sell = dp[False][idx+1] + prices[idx]
                    notSell = dp[stock][idx+1]
                    dp[stock][idx] = max(sell,notSell)
                else:
                    buy = dp[True][idx+1] - prices[idx] - fee
                    notBuy = dp[stock][idx+1]
                    dp[stock][idx] = max(buy,notBuy)



        return dp[False][0]
 


        # def dfs(idx,stock):

        #     if idx >= len(prices):
        #         return 0

        #     if (idx ,stock) in memo:
        #         return memo[(idx,stock)]
        #     if stock:
        #         sell = (dfs(idx+1,False) + prices[idx])
        #         notSell = dfs(idx+1,True)
        #         memo[(idx,stock)] = max(sell,notSell)
        #     else:
        #         buy = (dfs(idx+1, True) - prices[idx] - fee)
        #         notBuy = dfs(idx+1 ,False)
        #         memo[(idx,stock)] = max(buy,notBuy)

        #     return memo[(idx,stock)]

        # return dfs(0,False)