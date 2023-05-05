class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapify(piles)

        for _ in range(k):
           val = -heappop(piles)

           heappush(piles ,-(val - val//2))
        
        return -sum(piles)