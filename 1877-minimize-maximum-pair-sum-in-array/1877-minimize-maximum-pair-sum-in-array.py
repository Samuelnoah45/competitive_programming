class Solution:
    def minPairSum(self, nums: List[int]) -> int:       
        nums.sort()
        left = 0
        right = len(nums)-1
        maxPair=0
        while left < right:
            sums = nums[left] + nums[right]
            if maxPair < sums:
                maxPair = sums
            left += 1
            right-= 1
        return maxPair


        