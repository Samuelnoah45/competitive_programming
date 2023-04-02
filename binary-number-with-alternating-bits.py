class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check = ""
        while n != 0:
            if n&1==0  and check != "1":
                check = "1"
            elif n&1 !=0 and check != "0":
                check = "0"
            else:
                return False
            n >>= 1
      
        return True