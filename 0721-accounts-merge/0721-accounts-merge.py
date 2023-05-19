class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
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
                    
        for i in range(n):
            for j in range(i+1 ,n):
                val = set(accounts[i]).intersection(accounts[j])
                if accounts[i][0] == accounts[j][0] and len(val) > 1:
                    union(i ,j)
        Hash = defaultdict(list)

        for i in range(n):
            find(i)
        for i in range(n):
            Hash[find(i)].append(i)


        result = []
        for key in Hash:
            name = accounts[Hash[key][0]][0]
            email = set()
            for idx in Hash[key]:
                email.update(accounts[idx][1:])
              
            final = [name] +sorted(list(email))
            result.append(final)

        return result
            
  

        

        
