class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = {chr(97+i):chr(97+i) for i in range(26) }
        rank = {chr(97+i):1 for i in range(26) }
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
        
        for i in range(len(s1)):
            union(s1[i] ,s2[i])

        print(parent)
        ans = ""
        for ch in baseStr:
            pr = (find(ch))
            print(pr)
            for ch  in  parent:
                if parent[ch] == pr:
                    ans += ch 
                    break
        return ans