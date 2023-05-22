class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        parent = [i for i in range(n)]
        Hash = defaultdict(list)
        rank = [0]*(n+1)
        minDist = 0
        def find(x):
            if x == parent[x]:
                return x
            r = find(parent[x])
            parent[x] = r
            return r
            
        def union(x, y ,d):
            nonlocal minDist
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                minDist += d
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                    rank[rep_x] += rank[rep_y]
                else:
                    parent[rep_x] = rep_y
                    rank[rep_y] += rank[rep_x]


        connection = []
        for i in range(n):
            for j in range(i + 1 ,n):
                    xi , yi = points[i]
                    xj , yj = points[j]
                    val = abs(xi - xj) + abs(yi - yj)
                    connection.append([val ,(i,j)])
        connection.sort()
        visited = set()
        for  d , (x,y) in connection:
            if len(visited) <= n:
                union(x,y,d)
                visited.add(x)
                visited.add(y)
            else:
                break



        return minDist



        