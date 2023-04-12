class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        Hash = defaultdict(list)
        color = {}
        for item in dislikes:
            Hash[item[0]].append(item[1])
            Hash[item[1]].append(item[0])

        visited = set()
        ans = True
        def dfs(color , visited ,key ,cur):
            nonlocal ans
            visited.add(key)
            color[key] = cur
            cur = 1 - cur
            for ch in Hash[key]:
                if ch not in visited:
                    dfs(color ,visited ,ch ,cur)
                else:
                    if color[ch] == color[key]:
                        ans = False
        for key in Hash:
            if key not in visited:
                dfs(color ,visited ,key ,0)

        return ans