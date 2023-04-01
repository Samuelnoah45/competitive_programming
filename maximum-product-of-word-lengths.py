class Solution:
    def maxProduct(self, words: List[str]) -> int:

        Hash  = {}
        ans = 0
        for i , word in enumerate(words):
            res = 0
            for ch in word:
                mask = 0
                mask =1<<ord(ch)-97
                res |=mask 

            Hash[i] = res
            
        for i in Hash:
            for  j in Hash:
                if Hash[i]&Hash[j]==0:
                  ans =max(ans ,len(words[i])*len(words[j]))

        return ans