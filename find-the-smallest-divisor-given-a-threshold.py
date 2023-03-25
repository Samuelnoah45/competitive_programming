class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        def helper(md):
            total = 0
            for num in nums:
                total += ceil(num/md)
            if total <= threshold:
                return True
            return False

        while l < r:
            md = l + (r - l)//2

            if helper(md):
                r = md 
            else:
                l = md +1

        return l