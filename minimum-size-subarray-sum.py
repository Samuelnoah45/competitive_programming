class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        '''  
        1 1 1 2 1 1
        
        '''

        l = 0
        r = 0
        ans = len(nums) + 1
        sums = 0
        

        while r < len(nums):
            sums += nums[r]
            if sums < target:
                r += 1
            else:
                while  sums >= target :
                    ans = min(ans,r-l+1) 
                    sums -= nums[l]
                    if l == r:
                        return 1
                    l += 1
                r += 1

                
        return 0  if  ans == len(nums) + 1 else ans