class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)

        ans = [[0] * (N-2) for _ in range(N-2)]

        for i in range(N-2):
            for j in range(N-2):
                
                for di in range(3):
                    for dj in range(3):
                        ans[i][j] = max(ans[i][j], grid[i + di][j + dj])
        return ans