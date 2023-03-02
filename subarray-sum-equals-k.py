class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        res = 0
        hash = {0:1}
        for num in nums:
            sums += num
            if (sums -k) not in hash:
                 hash[sums] = hash.get(sums,0) + 1

            else:
                res += hash[sums-k]
                hash[sums] = hash.get(sums,0) + 1

            
        return res