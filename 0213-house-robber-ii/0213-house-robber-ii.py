class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def dfs(n ,_len ,memo):
            if n >= _len:
                return 0 

            if n in memo:
                return memo[n]
            memo[n] = max(nums[n]+ dfs(n+2,_len,memo) , dfs(n+1,_len,memo))

            return memo[n]

        return max(dfs(0,len(nums) - 1 ,{}) ,dfs(1,len(nums) ,{}))