class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash = {}
        ans = 0
        l = 0
        for r in range(len(fruits)):
            if len(hash) < 2 or fruits[r] in hash:
                hash[fruits[r]] = hash.get(fruits[r],0) + 1
                ans = max(ans ,r-l+1)
            else:
                while len(hash) == 2:
                    hash[fruits[l]] -= 1
                    if hash[fruits[l]] == 0: 
                        del hash[fruits[l]]
                    l += 1
                hash[fruits[r]] = hash.get(fruits[r],0) + 1

                
        return ans
                
                    


                



            
            
            

   
        return ans