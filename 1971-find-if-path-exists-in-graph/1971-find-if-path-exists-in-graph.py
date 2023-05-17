class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        rep = {i: i for i in range(n)}
        size = [1 for i in range(n)]
        def getRep(x):
            if rep[x] == x:
                return x
            r = getRep(rep[x])
            rep[x]=r
            return r

        for  x , y in edges:
            x_rep = getRep(x)
            y_rep = getRep(y)
            if x_rep != y_rep:
                
                if size[x_rep] > size[y_rep]:
                    rep[y_rep] = x_rep
                    size[x_rep] += size[y_rep]
                else:
                    rep[x_rep] = y_rep
                    size[y_rep] += size[x_rep]

        return getRep(source) == getRep(destination)




                



        
        