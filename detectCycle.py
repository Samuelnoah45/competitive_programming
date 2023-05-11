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