class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
    
        left = 0 
        right = len(nums)-1
        nums.sort()
        opration = 0
        
        while left < right:
            
            sums = nums[left] + nums[right]
            
            if sums== k:
                opration += 1
                left += 1
                right -= 1
            elif sums < k :
                left += 1
            else:
                right -= 1
        return opration
            
        