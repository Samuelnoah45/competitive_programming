class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans=[]    
        
        while len(nums) != 0:
           
            ans.append(nums.pop(0))
            if len(nums) != 0:
                ans.append(nums.pop())

           
        return ans

            
