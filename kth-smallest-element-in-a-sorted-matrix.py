class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap,-matrix[i][j])

                elif heap[0] < -matrix[i][j]:
                    heapreplace(heap,-matrix[i][j])
        

        return -heap[0]