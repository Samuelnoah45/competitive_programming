class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        arr =  [0] * (len(s) +1)
        strs = s
        for s , e , d in shifts:

            if d == 1:
                arr[s] += 1
                arr[e + 1] -= 1
            else:
                arr[s] -= 1
                arr[e + 1] += 1

        prifex = []

        for i in range(len(arr)):
            if len(prifex) == 0:
                prifex.append(arr[i])
            else:
                prifex.append(arr[i] +prifex[-1])
        ans = []
        ASCI_a = ord('a')
        for i, char in enumerate(strs):
            curr = (ord(char)-ASCI_a+prifex[i]) % 26
            
            ans.append(chr(curr+ASCI_a))
        

        return "".join(ans)