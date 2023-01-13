class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxValue=0
        piles.sort()
        length=len(piles)//3
        for i in range(length):
            piles.pop()
            maxValue+= piles.pop()
     
        return maxValue