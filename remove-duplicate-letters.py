class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        prev = Counter(s)
        stack = []
    
        for ch in s:
            while stack and prev[stack[-1]] > 0 and stack[-1] >= ch:
                if ch not in stack:
                    poped = stack.pop()
                else:
                    prev[ch] -=1
                    break

            if ch not in stack:
                stack.append(ch)
                prev[ch] -= 1
            

        return "".join(stack)