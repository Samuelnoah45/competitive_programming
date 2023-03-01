class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        '''  
        1 1 1 2 1 1
        
        '''

        l = 0
        ans = len(nums) + 1
        sums = 0
        
        for r in range(len(nums)):
            sums+=nums[r]

            while sums>=target:
                ans = min(ans, r-l+1)
                sums-=nums[l]
                l+=1
            
        
        return 0 if ans==len(nums)+1 else ans

