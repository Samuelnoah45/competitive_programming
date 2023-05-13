class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        for i in range(n):
            if group[i] == -1:
                    group[i] = m
                    m += 1
        groupOrder = defaultdict(set)
        groupDegree = [0]*m
        graphs = [defaultdict(list) for _ in range(m)]
        graphsDegree = [defaultdict(int) for _ in range(m)]
        members = [set() for _ in range(m)]
        
        tempAns = []
        for i in range(n):
            if len(beforeItems[i]) != 0:
                for num in beforeItems[i]:
                
                    if group[i] != group[num]:
                        if group[i] not in groupOrder[group[num]]:
                            groupOrder[group[num]].add(group[i])
                            groupDegree[group[i]] += 1
                        members[group[i]].add(i)
                        members[group[num]].add(num)
                    else:
                        graphs[group[num]][num].append(i)
                        graphsDegree[group[num]][i] += 1
                        members[group[num]].add(i)
                        members[group[num]].add(num)
            else:
                members[group[i]].add(i)

        
                 
        finalOrder = []
        GpOrderQue = deque()
        print(groupOrder)
        for i in  range(m):
            if groupDegree[i] == 0:
                finalOrder.append(i)
                GpOrderQue.append(i)


        while GpOrderQue:
            curGp = GpOrderQue.popleft()
            for node  in  groupOrder[curGp]:
                groupDegree[node] -= 1
                if groupDegree[node] == 0:
                    GpOrderQue.append(node)
                    finalOrder.append(node)
     
        result = []
        for num in finalOrder:
            myQue = deque()
            for el in members[num]:
                if graphsDegree[num][el] == 0:
                    myQue.append(el)
            ans = []
            while myQue:
                curNode = myQue.popleft()
                ans.append(curNode)
                for node in graphs[num][curNode]:
                    graphsDegree[num][node] -= 1
                    if graphsDegree[num][node] == 0:
                        myQue.append(node)

            result += ans
                
        return  result if len(result) == n else []