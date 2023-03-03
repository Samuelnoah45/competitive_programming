class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        ans = []

        for num in nums:

            if len(ans) == 0:
                ans.append(num)
            else:
                ans.append(ans[-1] + num)
        
        return ans