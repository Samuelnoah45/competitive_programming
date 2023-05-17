class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        parent = {}
        rank = {}

        directions = [(1, 0), (0, 1)]
        inbound = lambda x, y: x in range(n) and y in range(m)

        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 1
            if x == parent[x]:
                return x
            r = find(parent[x])
            parent[x] = r
            return r
            
        
        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                    rank[rep_x] += rank[rep_y]
                else:
                    parent[rep_x] = rep_y
                    rank[rep_y] += rank[rep_x]

        hashTable = {1: [{},{1,3,5}], 2: [{2,5,6}, {}],3: [{2,5,6}, {}], 4:[{2,5,6},{1,3,5}],5:[{},{}], 6:[{},{5,3,1}]}
        for i in range(n):
            for j in range(m):
                rr, rc = i, j + 1
                dr, dc = i + 1, j
                if inbound(rr,rc) and grid[rr][rc] in hashTable[grid[i][j]][1]:
                    union((i,j),(rr,rc))
                if inbound(dr,dc) and grid[dr][dc] in hashTable[grid[i][j]][0]:
                    union((i,j),(dr,dc))
      
        return find((0,0)) == find((n-1,m-1))