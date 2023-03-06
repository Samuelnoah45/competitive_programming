class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        count = 0
        
        prefix = list(accumulate(nums))
    
        for num in prefix:
            if num - k in hash:
                count += hash[num - k]
            hash[num] += 1

        return count