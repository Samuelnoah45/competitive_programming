class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        stack = []
        nums = nums + nums
        ans = [-1] *(len(nums)//2)
        
        for i in range(len(nums)):
            
            while stack and stack[-1][0] < nums[i]:
                val , idx = stack.pop()
                
                if idx < len(nums)//2:
                    ans[idx] = nums[i]
    
            stack.append([nums[i], i])
            
        return ans