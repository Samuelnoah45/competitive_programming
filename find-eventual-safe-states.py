class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graphs = {}
        color = [0]*len(graph)
        order = []
        for idx , adj in enumerate(graph):
            graphs[idx] = adj

        print(graphs)
        def dfs(node,color,graphs,order):
            if color[node] == 1:
                return False 
            color[node] = 1
            
            for nd in graphs[node]:
                if color[nd] == 2:
                    continue
                if  not dfs(nd,color,graphs,order):
                    return False 
            
            color[node] = 2
            order.append(node)
            return True 
            
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i,color,graphs,order)
    

        return sorted(order)