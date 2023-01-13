class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:       
        
        ans=[]
        for i in range(len(r)):
            newNums = nums[l[i]:r[i]+1]
            newNums.sort()
            inc = newNums[1] - newNums[0]
            flag = True
            for j in range(1,len(newNums)):
                print(newNums[j] - newNums[j-1] ,j)

                if  newNums[j] - newNums[j-1] != inc:
                    flag = False
                    break
            ans.append(flag)



            # if inc < 0:
            #     inc=-(inc) 
            
            # if newNums[-1] == newNums[0]+(len(newNums)-1)*inc:
            #     ans.append(True)
            # else:
            #     ans.append(False)
            # if ans[-1] == True:
            #     print(newNums)

        return ans


        