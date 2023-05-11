class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0]*n
        for fr , to in edges:
            graph[fr].append(to)
            indegree[to] += 1
            
        ans = [set() for i in range(n)]
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)
       
        while que:
            temp = que.popleft()

            for node in graph[temp]:
                ans[node].add(temp)
                ans[node].update(ans[temp])
                indegree[node] -= 1
                if indegree[node] == 0:
                    que.append(node)
                    
        for i in range(n):
            ans[i] = sorted(list(ans[i]))
        return ans