class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        direction = [(1,0) ,(-1,0) ,(0,1),(0 ,-1) ,(1,1) ,(-1,-1) ,(1,-1) ,(-1,1)]
        inbound = lambda x, y: x in range(n) and y in range(n)
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        
        que = deque([(0,0)])
        level = 0
        while que:
            level += 1
            for _  in range(len(que)):
                i , j = que.popleft()
                if [i,j] == [n-1 ,n-1]:
                    return level

                for di , dj in direction:
                    newi = di+i 
                    newj = dj+j

                    if inbound(newi ,newj) and grid[newi][newj] == 0:
                        que.append((i+di, j+dj))
                        grid[newi][newj] = 1

        return -1