class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = {}
        ans = set()
        for idx , room in  enumerate(rooms):
            graph[idx] = room

        que = deque([0])
        while que:
            poped = que.popleft()
            ans.add(poped)
            for node in graph[poped]:
                if node not in ans:
                    que.append(node)
            
        return len(ans) == len(rooms)