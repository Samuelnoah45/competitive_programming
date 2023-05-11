class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        degree = [0]*n
        ans = [0]*n

        for From , to in edges:
            graph[From].append(to)
            graph[to].append(From)
            degree[to] += 1
            degree[From] += 1
        que = deque()
        visited = set()
        for i in range(len(degree)):
            if degree[i] == 1:
                que.append(i)
                visited.add(i)

        while que:
            curNode = que.popleft()
            for node in graph[curNode]:
                if (ans[curNode] + 1) > ans[node]  and node not in visited:
                    ans[node] = (ans[curNode] + 1)
                degree[node] -= 1
                if degree[node] == 1 and node not in visited:
                    que.append(node)
                    visited.add(node)

        maxVal = max(ans)
        result = []
        print(ans)
        for i in range(len(ans)):
            if maxVal == ans[i]:
                result.append(i)
        return result