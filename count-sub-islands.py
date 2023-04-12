class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        
        count = 0
        def inbound(row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))
        sub = []
        def dfs(grid, row, col ,island):
                visited.add((row,col))
                island.append((row,col))
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and (new_row , new_col) not in visited and  grid[new_row][new_col] == 1:
                        dfs(grid, new_row, new_col ,island)

                return island
                
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if  grid2[i][j] == 1 and (i , j) not in visited:
                    sub.append(dfs(grid2 , i , j , []))
        
        print(sub)
        for i in sub:
            check = True
            for j in i:
                r,c = j
                if grid1[r][c] != 1:
                    check = False
                    break
            if check:
                ans+=1
        return ans