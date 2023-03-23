class Solution:
    def balancedString(self, s: str) -> int:

        hash = Counter(list(s))
        maxVal = len(s)//4
        over ={k: v - maxVal for k, v in hash.items() if v > maxVal}
        check = defaultdict(int)
        ans = len(s) + 1 
        l = 0


        if len(over) == 0:
            return 0

        counter = 0
        for r in range(len(s)):
            if s[r] in over:
                check[s[r]] += 1

                if  over[s[r]] == check[s[r]]:
                    counter += 1
        
            while counter == len(over):
                
                    print(s[l])
                    if s[l] in check:
                        check[s[l]] -= 1
                        if  check[s[l]] < over[s[l]]:
                            counter -= 1
                    ans = min(ans , (r-l + 1))
                    l += 1

        return ans