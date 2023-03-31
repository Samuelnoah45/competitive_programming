class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        ans = 0 

        while x != 0 or y != 0:
            if x == 0 and y&1 == 1:
                ans +=1
            elif y == 0 and x&1 == 1:
                ans +=1
            elif x&1 == 0 and y&1 == 1 or y&1 == 0 and x&1 == 1 :
                ans += 1
            x>>=1
            y>>=1
        

        return ans