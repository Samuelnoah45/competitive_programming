class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for fr , to in prerequisites:
            graph[fr].append(to)
            indegree[to] += 1
            
        ans = [set() for i in range(numCourses)]
        que = deque()
        for i in range(numCourses):
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
        result = []         
        for u , v  in queries:
            result.append(u in ans[v])
        return result