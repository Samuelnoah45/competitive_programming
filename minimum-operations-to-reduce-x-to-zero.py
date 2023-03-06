class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        hash ={0:-1}
        sum_ = 0
        maxL = 0
        x = sum(nums) - x
        if x == 0:
            return len(nums)
        for i, num in enumerate(nums):
            sum_ += num
            if sum_ - x  in hash:
                maxL = max(maxL , i - hash[ sum_ - x])
            if sum_ not in hash:
                hash[sum_] =  i

        return  len(nums) - maxL if maxL != 0 else -1