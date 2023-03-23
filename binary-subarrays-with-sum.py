class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        count = 0

        prefix = list(accumulate(nums))
    
        for num in prefix:
            if num - goal in hash:
                count += hash[num - goal]
            hash[num] += 1

        return count