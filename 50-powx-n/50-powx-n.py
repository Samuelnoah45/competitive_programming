class Solution:
    def myPow(self, x: float, n: int) -> float:
        pos = False
        ans = 0
        if n == 0:
            return 1
        if n > 0:
            pos = True 
        n = abs(n)

        def pow_(x , n):
            if n == 1:
                return x
            else:
                if n % 2 == 0:
                    return  pow_(x*x, n/2 )
                else:
                    return x * pow_(x, n - 1)

        ans = pow_(x ,n)
        if not pos:
            return 1/ans

        return  ans