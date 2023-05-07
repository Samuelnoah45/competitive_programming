class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        que = deque()
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        inbound = lambda x , y: x in range(len(mat)) and y in range(len(mat[0]))
    
        visited = set()
        ans = [[0]*len(mat[0]) for i in range(len(mat))]

        print(ans)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.append((i,j))
                    visited.add((i,j))
        level = 0

        while que:
            level += 1
            for _ in range(len(que)):
               
                x,y = que.popleft()

                for r,c in direction:
                    nr, nc = r + x, c + y

                    if inbound(nr,nc) and (nr,nc) not in visited:
                        ans[nr][nc] = level
                        que.append((nr,nc))
                        visited.add((nr,nc))
        return ans