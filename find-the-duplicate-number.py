class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i)] < 0: return abs(i)
            nums[abs(i)] *= -1