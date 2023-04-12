class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for  i, b1 in enumerate(bombs):
            for  j, b2 in enumerate(bombs):
                if i != j:
                    dist = math.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)
                    if dist <= b1[2]:
                        graph[i].append(j)
        visited = set()
        count  = 0
        ans = 0
        def dfs(visited ,node):
            nonlocal count 
            visited.add(node)
            count += 1
            for key in graph[node]:
                if key not in visited:
                    dfs(visited ,key)
        print(graph)
        nodes = []
        for bm in graph:
                nodes.append(bm)
        
        for nd in nodes:
            dfs(visited ,nd)
            visited.clear()
            ans = max(ans ,count)
            count = 0
        if not  nodes:
            ans = 1
        return ans