class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        minDist = 0

        def find(x):
            return parent[x]
        
        def union(x, y,d):
            nonlocal minDist
            x_rep = find(x)        
            y_rep = find(y)
            if x_rep != y_rep:
                minDist += d
                for i in range(len(parent)):
                    if parent[i] == y_rep:
                        parent[i] = x_rep


        connection = []
        for i in range(n):
            for j in range(i + 1 ,n):
                    xi , yi = points[i]
                    xj , yj = points[j]
                    val = abs(xi - xj) + abs(yi - yj)
                    connection.append([val ,(i,j)])
        connection.sort()

        for  d , (x,y) in connection:
            if len(set(parent)) != 1:
                union(x,y,d)
            else:
                break



        return minDist



        