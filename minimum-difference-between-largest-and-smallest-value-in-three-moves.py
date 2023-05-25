class Solution:
    def minDifference(self, nums: List[int]) -> int:


        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        direction = [(3,n-1) ,(0,n-4) ,(1,n-3) ,(2,n-2)]

        ans = []

        for l ,r in direction:
            ans.append(nums[r] - nums[l])

        return min(ans)