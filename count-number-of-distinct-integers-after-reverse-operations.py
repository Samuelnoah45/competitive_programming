class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(set(nums) | {int(str(n)[::-1]) for n in nums})