class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        def fun(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)

        return fun(a,b)