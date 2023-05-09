class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [[1,0],[0,1] ,[-1,0],[0,-1]]
        inbound = lambda x , y : x in range(len(maze)) and y in range(len(maze[0]))


        que = deque([entrance])
        level = 0
        visited = set()

        visited.add(tuple(entrance))
     
        while que:
            for _ in range(len(que)):
                i , j = que.popleft()
                
    
                for x , y in directions:
                    newX = i + x
                    newY = j + y
                    if not inbound(newX ,newY) and [i,j] != entrance:
                        return level
                    
                    if  inbound(newX,newY) and maze[newX][newY] == "." and (newX, newY) not  in visited:
                        que.append([newX,newY])
                        visited.add((newX, newY))
            level += 1

        return -1