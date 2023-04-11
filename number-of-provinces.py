class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Hash = defaultdict(list)
        visited = set()
        for idx, cons in enumerate(isConnected):
            for idx2, con in enumerate(cons):
                if idx2 != idx and con!=0:
                    Hash[idx].append(idx2)
            if not Hash[idx]:
                print(idx)
        ans = 0
        def dfs(key,visited):
            visited.add(key)
            for sub in Hash[key]:
                if sub not in visited:  
                    dfs(sub ,visited)

        for key in Hash:
            if key not in visited:
                ans += 1
                dfs(key ,visited)


        return ans