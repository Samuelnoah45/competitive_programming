class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.matrix.insert(0, [0]*len(matrix[0]))
        row = 0
        col = len(matrix[0]) 
        for rows in  self.matrix:
            rows.insert(0, 0)  
            row += 1  
        
        for i in range(1,row):
            for j in range(1,col+1):
                up = self.matrix[i-1][j] 
                left = self.matrix[i][j-1] 
                diag = self.matrix[i-1][j-1] 

                self.matrix[i][j] += up + left - diag
            
            print(self.matrix[i])
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        Ul = [row1 ,col1]
        Ur = [row1 ,col2+1]
        Ll = [row2+1 ,col1]
        Lr = [row2+1,col2+1]

        bigSum = self.matrix[ Lr[0] ][ Lr[1] ]
        upperSum = self.matrix[ Ur[0] ][ Ur[1] ]
        leftSum = self.matrix[ Ll[0] ][ Ll[1] ]
        diag = self.matrix[ Ul[0] ][ Ul[1] ]

        print(bigSum - upperSum - leftSum + diag)

        return (bigSum - upperSum - leftSum + diag)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)