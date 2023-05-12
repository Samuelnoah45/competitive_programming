class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        graph = defaultdict(list)
        degree = [0]*n
        for From , to in  enumerate(edges):
            if to >= 0:
                graph[From].append(to)
                degree[to] += 1

        que = deque()
        for i in range(n):
            if degree[i] == 0:
                que.append(i)
        
        while que:
            curNode = que.popleft()
            for node in graph[curNode]:
                degree[node] -= 1
                if degree[node] == 0:
                    que.append(node)

        visited = set()
        print(degree)
        if sum(degree) == 0:
            return -1
        for i in range(n):
            if degree[i] != 0:
                que.append(i)
                count = 0
                while que:
                    curNode = que.popleft()
                    if graph[curNode][0]  in visited:
                        break
                    count += 1
                    for node in graph[curNode]:
                        que.append(node)
                        visited.add(node)

                ans = max(ans ,count)         
        return ans