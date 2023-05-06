class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        if len(tasks) == 1:
            return [0]

        for idx , task in enumerate(tasks):
            task.append(idx)
        tasks = sorted(tasks ,key=lambda x: x[0])
        heap = []
        time = 0
        ans = []
        r = 0
        while r < len(tasks):
            while  r < len(tasks) and  tasks[r][0] <= time:
                heappush( heap ,(tasks[r][1] ,tasks[r][2]))
                r += 1
            else:
                if heap:
                    ptime , idx = heappop(heap)
                    ans.append(idx)
                    time += ptime
                else:
                    time = tasks[r][0] 
        while heap:
            ptime , idx = heappop(heap)
            ans.append(idx)
            

        return ans