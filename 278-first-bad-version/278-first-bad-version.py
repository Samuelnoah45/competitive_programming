# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n

        while l <= r:

            md = l + (r-l)//2
            print(l)
            if isBadVersion(md):
                r = md -1
            else:
                l = md + 1

        return  l


            
        