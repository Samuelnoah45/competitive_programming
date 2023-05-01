class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        
        visited = set(deadends)
        que = deque(["0000"])
        if "0000" in visited:
            return -1
        if "0000" == target:
            return 0
        level = 0
        visited.add("0000")
        
        while que:
            level += 1
            for _ in range(len(que)):
                key = list(map(int,que.popleft()))

                for i in range(4):
                    key[i] = (key[i]+1)%10
                    check = "".join(map(str,key))
                    if check not in visited:
                        que.append(check)
                        visited.add(check)
                    
                    if check == target:
                        return level

                    key[i] = (key[i]-2)%10
                    check = "".join(map(str,key))
                    if check not in visited:
                        que.append(check)
                        visited.add(check)
                    

                    if check == target:
                        return level

                    key[i] = (key[i] + 1)%10
                    
                
                

        return -1