class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter=0
        print(len(strs))
        print(len(strs[0]))
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
              if  strs[j][i] > strs[j+1][i]:
                    print(i,strs[j][i],strs[j+1][i])
                    counter+=1
                    
                    break

        return  counter