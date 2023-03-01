class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        hash2 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            hash1[s1[i]] = hash1.get(s1[i], 0) + 1
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1
        
        l = 0 
        r = len(s1)-1
        while r < len(s2):
            if hash2 == hash1:
                return True
            else:
                hash2[s2[l]] -= 1
                if hash2[s2[l]] == 0:
                    del hash2[s2[l]]
                
                if r == len(s2)-1:
                    break
                else:
                    hash2[s2[r+1]] = hash2.get(s2[r+1],0) + 1 
            r += 1
            l += 1


        return False