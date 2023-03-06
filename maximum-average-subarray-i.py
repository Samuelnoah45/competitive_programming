class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sums = sum(nums[0:k])
        ans = sums/k
        l = 0
        r = k
        while r < len(nums):
          sums -= nums[l]  
          sums += nums[r]
          ans = max(ans, sums/k)

          l += 1
          r += 1  

        return ans