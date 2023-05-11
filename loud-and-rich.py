class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        inDegree = [0]*len(quiet)
        ans = [set() for i in range(len(quiet))]
        graph = defaultdict(list)

        for rich , poor in richer:
            graph[rich].append(poor)
            inDegree[poor] += 1
        que = deque()
        for i in range(len(quiet)):
            if inDegree[i] == 0:
                que.append(i)

        while que:
            temp = que.popleft()
            for node in graph[temp]:
                ans[node].add(temp)
                ans[node].update(ans[temp])

                inDegree[node] -= 1
                if  inDegree[node] == 0:
                    que.append(node)
        result = [x for x in range(len(quiet))]
        
        for i in range(len(ans)):
            newVal  = [(quiet[i] ,i)]
            if len(ans[i]) != 0:
                for num in ans[i]:
                    newVal.append((quiet[num] ,num))
             
                minVal = min(newVal)
                result[i] = minVal[1] 
        
                
                
        return  result