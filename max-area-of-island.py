class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        ans = 0
        area = 0
        def dfs(grid, visited, row, col):
                visited[row][col] = True
                nonlocal area
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and not visited[new_row][new_col] and  grid[new_row][new_col] == 1:
                        area += 1
                        dfs(grid, visited, new_row, new_col)
                        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j] == 1 and not visited[i][j]:
                    area+=1
                    dfs(grid ,visited , i , j)
                    ans = max(ans , area)
                    area = 0
    
    
        return ans