class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        res = 0
        hash = {0:1}
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        sums = 0
        for num in nums:
            sums += num
            if (sums -k) not in hash:
                 hash[sums] = hash.get(sums,0) + 1

            else:
                res += hash[sums-k]
                hash[sums] = hash.get(sums,0) + 1

            
        return res