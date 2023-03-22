class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []

        for ch in s:
            if ch == "(":
                stack.append("(")

            else:
                ch2 = stack.pop()
                if ch2 == "(":
                        if not stack or stack[-1] == "(":
                            stack.append(1)
                        else:
                            num = stack.pop()
                            stack.append(num + 1)       
                else:
                        num = stack.pop()
                        if not stack or stack[-1] == "(":
                            stack.append(ch2 * 2)
                        else:
                                num = stack.pop()
                                stack.append(num + (ch2*2))  
             
        return stack[0]

        