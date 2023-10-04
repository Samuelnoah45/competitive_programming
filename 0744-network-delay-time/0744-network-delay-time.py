import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for par ,ch  , weight in times:
            graph[par].append((ch ,weight))
        def dijkstra(graph, start):
            visited = set()
            distances = {node: float('inf') for node in range(1,n+1)}
            distances[start] = 0
            priority_heap = [(0,start)]

            while priority_heap:
                distance , node  = heapq.heappop(priority_heap)

                if node in visited:
                    continue 
                
                for child ,weight in graph[node]:
                    sums = distance + weight
                    if sums < distances[child]:
                        distances[child] = sums
                        heapq.heappush(priority_heap, (sums, child))
            return distances
        ans= dijkstra(graph,k)
        final  = max(ans.values())
        if final  != float('inf') :
            return  final

        return -1


            

        