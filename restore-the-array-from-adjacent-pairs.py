class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        nums = set()
        n = (len(adjacentPairs)+1)
        degree = defaultdict(int)
        ans = ["r"]*n
        visited = set()
        for From , to in adjacentPairs:
            graph[From].append(to)
            nums.add(to)
            nums.add(From)
            graph[to].append(From)
            degree[to] += 1
            degree[From] += 1 
        idxMemory = {}
        que = deque()
        for i in nums:
            if degree[i] == 1:
                que.append(i)
                if ans[0] == "r":
                    ans[0] = i
                    idxMemory[i] = 0
                    visited.add(i)
                else:
                    ans[-1] = i
                    idxMemory[i] = n - 1
                    visited.add(i)
      
        while que:
            curNode = que.popleft()

            for node in graph[curNode]:
                ID = idxMemory[curNode] 
                if node not in visited:
                    if ID + 1 < (n)  and ans[ID + 1] == "r":
                        ans[ID+ 1] = node
                        idxMemory[node] =  ID + 1
                        que.append(node)
                        visited.add(node)
                    elif ID - 1 > 0 and ans[ID - 1] == "r":
                        ans[ID - 1] = node
                        idxMemory[node] =  ID + 1
                        que.append(node)
                        visited.add(node)


        
        return ans