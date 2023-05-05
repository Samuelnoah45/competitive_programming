class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                n ,m =nums1[i] ,nums2[j]
                if len(heap) < k:
                    heappush(heap,(-(n+m),-n, -m))

                elif heap[0] < (-(m+n) ,-n, -m):
                    heappop(heap)
                    heappush(heap,(-(m+n) ,-n, -m))
                else:
                    break 
        

        return [(-num1 ,-num2) for sums , num1 ,num2 in heap]