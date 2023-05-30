class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(idx , total ):
            if idx == len(nums):
                return 1 if total == target else 0
            
            if (idx,total) in memo:
                return memo[(idx,total)]
            
            memo[(idx,total)] = (dfs(idx+1 ,total+nums[idx]) + dfs(idx+1 ,total-nums[idx]))
            return memo[(idx,total)]
            
        return dfs(0,0)     
        