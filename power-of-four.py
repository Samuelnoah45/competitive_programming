class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True
        if n == 0:
            return False
        def checkPower( num ):
            if num % 4 != 0:
                return False
            else:
                if num == 4:
                    print(num)
                    return True
                else:
                    return  checkPower( num // 4)

        return checkPower(n)