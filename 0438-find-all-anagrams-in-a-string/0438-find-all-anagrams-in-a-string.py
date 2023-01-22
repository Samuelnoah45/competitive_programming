class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = len(p)-1
        ans = []
        scount = {}
        pcount = {}
        if len(s) < len(p):
            return []
            
        for i in range(len(p)):
            if s[i] in scount:
                scount[s[i]] += 1
            else:
               scount[s[i]] = 1

            if p[i] in pcount:
                pcount[p[i]] += 1
            else:
               pcount[p[i]] = 1


        while right < len(s):
            if scount == pcount:
                ans.append(left)
            
            scount[s[left]] -=1
            if scount[s[left]]==0:
                del scount[s[left]]

            if right +1 >= len(s):
                break

            if s[right+1] in  scount:
               scount[s[right+1]] += 1
            else:
                scount[s[right+1]] =1

            left += 1
            right += 1
            

        return ans
