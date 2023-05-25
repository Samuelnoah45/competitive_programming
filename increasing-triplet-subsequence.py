class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        x = inf
        y = inf

        for n in  nums:
            if x >= n:
                x = n
            elif y >= n:
                y = n
            else:
                return True
        return False