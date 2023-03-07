class Solution:
    def decodeString(self, s: str) -> str:

        numStack =[]
        strStack = []
        ans = ""
        r = 0
        if len(s) == 1:
            if s.isnumeric():
                return ""
            else:
                return s
        while r < len(s):
            if s[r].isnumeric():
                num = ""
                while r < len(s) and s[r] != '[' :
                    print(s[r])
                    num +=  s[r]
                    r += 1
                if r < len(s):
                    strStack.append(s[r])
                numStack.append(int(num))
            elif s[r] != "]":
                strStack.append(s[r])
            else:
                
                check = strStack.pop()
                temp = ""
                while check != "[":
                    temp = check + temp
                    check = strStack.pop()

                strStack.append(temp*numStack.pop())
            r += 1
                
        return "".join(strStack)
       \

                
                

        