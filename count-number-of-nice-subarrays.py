class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        res = 0
        hash = {0:1}

        nums = [0 if num%2 ==0 else 1 for num in nums]
        prefix = list(accumulate(nums))
       
        sums = 0
        for sum_ in prefix:
            if (sum_ -k)  in hash:
                res += hash[sum_ -k]
            hash[sum_] = hash.get(sum_,0) + 1

        return res