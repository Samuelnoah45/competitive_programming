class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for w in nums:
            ans += count[w]
            count[w] += 1
        return ans