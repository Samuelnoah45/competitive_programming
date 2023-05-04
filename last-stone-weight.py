class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for num in stones:
            heap.append(-num)

        heapify(heap)

        while heap and len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x !=  y:
                newVal = y - x
                heapq.heappush(heap,newVal)
      
    
        if len(heap) == 0:
            return 0

        return -heap[0]