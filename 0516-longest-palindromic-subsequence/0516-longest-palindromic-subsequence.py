class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1  = s 
        text2 = s[::-1]
        l1 =  l2 = len(s)
        memo = {}
        def dep(idx1 ,idx2):
            if idx1 >= l1 or idx2 >= l2:
                return 0
            if (idx1 ,idx2) in memo:
                return memo[(idx1,idx2)]
            if text1[idx1] ==  text2[idx2]:
                memo[(idx1,idx2)] = dep(idx1+1 ,idx2+1) + 1
                return memo[(idx1,idx2)]
            else:
                 memo[(idx1,idx2)]= max(dep(idx1 ,idx2+1),dep(idx1+1 ,idx2))
                 return memo[(idx1,idx2)]
            
        return  dep(0,0)
            
        