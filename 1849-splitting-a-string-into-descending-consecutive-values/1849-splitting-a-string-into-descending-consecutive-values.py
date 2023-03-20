class Solution:
    def splitString(self, s: str) -> bool:

        cur = []

        def back(idx):

            if idx >= len(s):
                return len(cur) >=2
            for i in range(idx ,len(s)):
                print(s[idx:i+1] ,idx)
                val = int(s[idx:i+1])
    
                if len(cur) == 0 or val == cur[-1] -1:
                    cur.append(val)
                    if back(i+1):
                        return True
                    cur.pop()
            return False
        return back(0)