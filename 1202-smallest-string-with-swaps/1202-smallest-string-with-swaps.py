class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

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

        for x , y in pairs:
            union(x,y)
        Hashidx = defaultdict(list)
        HashL = defaultdict(list)

        for i in range(n):
           pr = find(i)
           Hashidx[pr].append(i)
           HashL[pr].append(s[i])
        ans = list(s)
        for key in Hashidx:
            index , letter  = sorted(Hashidx[key]),sorted(HashL[key])
            for i in range(len(index)):
                ans[index[i]] = letter[i]


        return "".join(ans)

        