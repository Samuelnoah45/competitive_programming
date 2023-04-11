class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        count = 0
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))

        def dfs(image, visited, row, col ,prcl):
                visited[row][col] = True
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and not visited[new_row][new_col] and  image[new_row][new_col]== prcl:
                        image[new_row][new_col] = color
                        dfs(image, visited, new_row, new_col ,prcl)
        dfs(image,visited ,sr ,sc , image[sr][sc])
        image[sr][sc] = color

        return image