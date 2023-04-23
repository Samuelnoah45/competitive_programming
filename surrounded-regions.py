class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        count = 0
        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))
        ans = 0
        area = 0
        def dfs(board, visited, row, col ,arr ,arr2):
                visited[row][col] = True
                nonlocal area
                check = True
                arr2.append((row , col))
                for row2 , col2 in directions:
                    if not inbound(row+row2, col+col2):
                        check = False
                if check:
                    arr.append((row , col))
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and not visited[new_row][new_col] and  board[new_row][new_col] == "O":                  
                        dfs(board, visited, new_row, new_col ,arr ,arr2)
                return arr ,arr2
                        
        change = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  board[i][j] == "O" and not visited[i][j]:
                    arr = []
                    arr2 = []
                    result ,result2 = dfs(board ,visited , i , j ,arr ,arr2)
                    if len(result) == len(result2):
                        change.append(result)

        for ch in change:
            for i , j in ch:
                board[i][j] = "X"