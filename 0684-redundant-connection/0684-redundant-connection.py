class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ans = [-1 ,-1]
        rep = {i: i for i in range(n)}
        size = [1 for i in range(n)]
        def getRep(x):
            if rep[x] == x:
                return x
            r = getRep(rep[x])
            rep[x]=r
            return r

        for  x , y in edges:
            x_rep = getRep(x-1)
            y_rep = getRep(y-1)
            if x_rep != y_rep:
                if size[x_rep] > size[y_rep]:
                    rep[y_rep] = x_rep
                    size[x_rep] += size[y_rep]
                else:
                    rep[x_rep] = y_rep
                    size[y_rep] += size[x_rep]
            else:
                ans[0] ,ans[1] = x , y
                

        return ans