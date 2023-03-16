class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def check(m , cur ,k):
            if m == 1:
                return cur
            if pow(2,m-1)//2 < k:
                print(cur)
                return  check(m - 1 ,1 - cur ,k - pow(2,m -1)/2)
            else:
                print(cur)
                return  check(m - 1 ,cur ,k)

        
        
        return check(n ,0 , k)