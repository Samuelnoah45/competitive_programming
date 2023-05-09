class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = [0]*numCourses
        order = []
        for cr , pre in prerequisites:
            graph[pre].append(cr)
           
        def dfs(node,color,graph,order):
            if color[node] == 1:
                return False 
            color[node] = 1
            
            for nd in graph[node]:
                if color[nd] == 2:
                    continue
                if  not dfs(nd,color,graph,order):
                    return False 

            color[node] = 2
            order.append(node)
            return True 
            
        for i in range(numCourses):
            if color[i] == 0:
                print(i)
                if not dfs(i,color,graph,order) :
                    return False
        
        return True