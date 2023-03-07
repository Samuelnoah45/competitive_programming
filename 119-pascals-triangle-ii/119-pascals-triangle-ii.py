class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = []
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex +1):
            if i == 0:
                ans = [1]
            if i == 1:
                ans = [1,1]
            else:
                temp = []
                for i in range(len(ans) -1):
                    temp.append( ans[i] + ans[ i+1 ] )
                    print(ans)
                ans = [1] + temp + [1]



        return ans