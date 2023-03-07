class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        else:
            prevArr = self.getRow(rowIndex -1)
            temp = []
            for i in range(len(prevArr) -1):
                temp.append(prevArr[i] + prevArr[i +1])
                
            return  [1] + temp + [1]

        