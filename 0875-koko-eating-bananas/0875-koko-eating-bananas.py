class Solution:
        def minEatingSpeed(self, piles: List[int], H: int) -> int:
            
            maxVal = max(piles)+1
            minVal  = 0

            hr = len(piles)
            result = maxVal
            while minVal + 1 < maxVal:
                mid =( maxVal + minVal) //2
                count = 0
                for ban in piles:
                    count += ceil(ban/mid)
                    
                if count <= H:
                    maxVal = mid
                    
                else:
                    minVal = mid
            
            return maxVal

                    
           