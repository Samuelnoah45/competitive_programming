class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False 
        Hash = Counter(deck)
        arr = list(Hash.values())

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b,a%b)
        ans = arr[0]
        for  i in range(1 , len(arr)):
            ans =gcd(ans ,arr[i])

        return ans != 1