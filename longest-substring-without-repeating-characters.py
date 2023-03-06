class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        right  = 0
        maxVal = 0
        strs = set()

        while right < len(s):
            if   s[right] not in  strs:
                 strs.add(s[right])
                 right += 1
                 
            else:
                strs.remove(s[left])
                left +=1
            maxVal = max(maxVal,len(strs))

        return  maxVal