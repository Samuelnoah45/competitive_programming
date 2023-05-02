class Solution:
    def racecar(self, target: int) -> int:
        que = deque([(0,1)])
        visited = set([(0,1)])
        level = 0
        
        while que:
            for _ in range(len(que)):
                pos, speed = que.popleft()

                if pos == target:
                    return level
                if (pos + speed, speed * 2) not in visited:
                    que.append((pos + speed, speed * 2))
                    visited.add((pos + speed, speed * 2))

                if speed > 0 and (pos, -1) not in visited:
                    que.append((pos, -1))
                    visited.add((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    que.append((pos, 1))
                    visited.add((pos, 1))

            level += 1