class Solution:
    def __init__(self):
        self.n = 0
        self.ans = ''
    def findKthBit(self, n: int, k: int) -> str:
        def recur(leng ,s):
            if leng == 0:
                self.ans = s
                return 
            rev = list(s[::-1])
            temp = ""
            for i in range(len(rev)):
                if rev[i] == "1":
                    temp = temp + "0"
                else:
                    temp = temp + "1"
     
            return recur(leng - 1 , s + "1" + temp)

        recur(n ,"0")
        return self.ans[k-1]