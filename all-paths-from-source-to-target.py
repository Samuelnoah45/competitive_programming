class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        Hash = defaultdict(list)
        ans = []
        end = len(graph) - 1
        for idx , item in  enumerate(graph):
            Hash[idx] = item

        def dfs(node ,path):
            nonlocal end
            path = path +[node]
            if node == end:
                ans.append(path)
            for key  in Hash[node]:
                dfs(key ,path)
        dfs(0 ,[])   
           
        return ans