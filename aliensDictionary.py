#User function Template for python3
from collections import defaultdict ,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        for i in range(len(alien_dict) -1 ):
            
            edges = self.comper(alien_dict[i] ,alien_dict[i+1])
            
            if edges:
               
                graph[edges[0]].append(edges[1])
                degree[edges[0]] = 0 if  edges[0] not in degree else degree[edges[0]]
                degree[edges[1]] += 1
            
        que = deque()
        
        for i in range(k):
            if not degree[chr(97+i)]:
                que.append(chr(97+i))
        order = []
       
        while que:
            curNode = que.popleft()
            order.append(curNode)
            for nbr in graph[curNode]:
                degree[nbr] -=1 
                if not degree[nbr]:
                    que.append(nbr)
      
        return "".join(order)
        
                


    def comper(self , str1 , str2 ):
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                return (str1[i] ,str2[j])
            i += 1 
            j += 1