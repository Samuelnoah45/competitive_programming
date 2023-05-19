class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        parent = [[i, float("inf")] for i in range(n+1)]
        rank = [0]*(n+1)

        def find(x):
            if x == parent[x][0]:
                return x
            parent[x][0] = find(parent[x][0])
            return parent[x][0]
            
        
        def union(x, y, dis):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if rank[rep_x] >= rank[rep_y]:
                    new_dis = min(dis, parent[rep_y][1], parent[rep_x][1])
                    parent[rep_y] = parent[rep_x]
                    rank[rep_x] += rank[rep_y]
                    parent[rep_x][1] = new_dis
                else:
                    new_dis = min(dis, parent[rep_y][1], parent[rep_x][1])
                    parent[rep_x] = parent[rep_y]
                    rank[rep_y] += rank[rep_x]
                    parent[rep_y][1] = new_dis
            else:
                new_dis = min(dis, parent[rep_x][1], parent[rep_y][1])
                parent[rep_x][1] = new_dis

        for x , y , d  in roads:
            union(x, y, d)

        start = find(1)
        
        return parent[start][1]

