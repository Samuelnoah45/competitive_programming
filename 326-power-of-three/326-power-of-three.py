class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        def checkPower( num ):
            if num % 3 != 0:
                return False
            else:
                if num == 3:
                    print(num)
                    return True
                else:
                    return  checkPower( num // 3)

        return checkPower(n)