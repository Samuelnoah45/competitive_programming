class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashT = Counter(t)
        left, right = 0, 0
        defdict = defaultdict(int)
        ans = ''
        
        count_completed = 0
 
        for right in range(len(s)):
        
            defdict[s[right]] += 1
                
            if defdict[s[right]] == hashT[s[right]]:
                count_completed += 1

            while count_completed == len(hashT):
                if not ans or  right - left + 1 < len(ans):
                        ans = s[left:right+1]

                if s[left] in t:
                    defdict[s[left]] -= 1

                if defdict[s[left]] < hashT[s[left]]:
                    count_completed -= 1

                left += 1
                       
        return ans