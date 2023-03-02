class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        backward = [1]
        forward = [1]
        for i in range(len(nums)):
            forward.append(forward[-1] * nums[i] )
            backward.append(backward[-1] * nums[-(i+1)] )     
        backward.reverse()
        
        
        for i in range(1,len(backward)):
            left = forward[i -1]
            right = backward[i]
            ans.append(left * right)
        
        
        return ans