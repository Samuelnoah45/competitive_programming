class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {
            "a":"a",
            "e":"e",
            "i":"i",
            "u":"u",
            "o":"o",
        }
        
        l = 0 
        r = k-1
        count =  0
        ans = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
                ans +=1
        
        while r < len(s)-1:
            if s[r+1] in vowel:
                count += 1
            if s[l] in vowel:
                count -= 1
            print(count,l,r)
            ans = max(ans,count)
            r += 1
            l += 1
        

        
    
        


        return ans
        