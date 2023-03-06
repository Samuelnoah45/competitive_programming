class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     
        hash = {}

        l = 0
        ans = 0
        freq = -1

        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r],0) + 1
            freq = max(freq, hash[s[r]])
            
            while  (r-l+1 - freq  ) > k:
                hash[s[l]] -= 1
                l += 1
            ans = max(ans , r-l+1)

        return ans















        return 0