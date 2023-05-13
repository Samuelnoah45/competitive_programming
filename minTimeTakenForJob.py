from typing import List
from collections import defaultdict,deque



from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list) 
        degree = [0]*(n+1)
        ans = [0] * (n+1)
        
        for From , to in edges:
            graph[From].append(to)
            degree[to] += 1
            
        que = deque()
        for i in range(n+1):
            if degree[i] == 0:
                que.append(i)
                ans[i] = 1
                
        que.popleft()       
        
        while que:
            
            curNode  = que.popleft()
            
            for node in graph[curNode]:
                degree[node] -= 1
                if degree[node] == 0:
                    nextTime = ans[curNode] + 1
                    ans[node] = nextTime
                    que.append(node)
        ans = [str(x) for x in  ans]
                    
        return " ".join(ans[1:])