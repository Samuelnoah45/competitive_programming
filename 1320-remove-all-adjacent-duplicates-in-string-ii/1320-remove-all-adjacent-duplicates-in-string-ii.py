class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])

        
        return ''.join([letter * count for letter, count in stack])
            
        