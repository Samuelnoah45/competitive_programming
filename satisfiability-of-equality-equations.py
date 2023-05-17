class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parent = {chr(97+i):chr(97+i) for i in range(26) }
        rank = {chr(97+i):1 for i in range(26) }

        def find(x):
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

        

        notEqual = []
        for eq in  equations:
            if eq[1] == "=":
                union(eq[0] ,eq[3])
            else:
                notEqual.append((eq[0] ,eq[3]))

        for x , y in notEqual:
            if find(x) == find(y):
                return False  


        return True