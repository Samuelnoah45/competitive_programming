class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # row of node
        row = [0]*(k + 1)
        rowGraph = defaultdict(list)
        rowDegree = [0]*(k+1)

        for x , y in rowConditions:
            rowGraph[x].append(y)
            rowDegree[y] += 1

        que = deque()
        for i in range(1 ,k+1):
            if rowDegree[i] == 0:
                que.append(i)
        level = 0
        while que:
            node = que.popleft()
            row[node] = level
            for nbr in rowGraph[node]:
                rowDegree[nbr] -= 1
                if rowDegree[nbr] == 0:
                    que.append(nbr)
        
            level += 1
        
        # col of node 
        if sum(rowDegree) != 0:
            return []

        col = [0]*(k + 1)
        colGraph = defaultdict(list)
        colDegree = [0]*(k+1)

        for x , y in colConditions:
            colGraph[x].append(y)
            colDegree[y] += 1

        que = deque()
        for i in range(1 ,k+1):
            if colDegree[i] == 0:
                que.append(i)
        level = 0
        while que:
            node = que.popleft()
            col[node] = level
            for nbr in colGraph[node]:
                colDegree[nbr] -= 1
                if colDegree[nbr] == 0:
                    que.append(nbr)
        
            level += 1
        if sum(colDegree) != 0:
            return []

        print(row , col) 

        matrix = [[0 for _ in range(k)] for _ in range(k) ]
       
        for i  in range(1 , k+1):
            matrix[row[i]][col[i]] = i

        return matrix