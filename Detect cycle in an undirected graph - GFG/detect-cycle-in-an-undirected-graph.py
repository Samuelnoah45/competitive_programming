from typing import List
from collections import  deque, defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		graph = {}
	
		for idx , val  in  enumerate(adj):
		  graph[idx] = val
		 
		que = deque()
		parent  = defaultdict(int)
		
		visited = set()
	    for i in range(V):
	        if i not in visited:
	            que.append(i)
	            visited.add(i)
	            while que:
	                curNode = que.popleft()
	                for child in graph[curNode]:
	                    if child not in visited:
	                        que.append(child)
	                        parent[child] = curNode
	                        visited.add(child)
	                    elif parent[curNode] != child:
	                        return True
        return False
	                    
	                    
	                    
	                    
	                    
                    
                    	        
            
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends