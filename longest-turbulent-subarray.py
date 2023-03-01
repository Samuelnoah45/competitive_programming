class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        '''
        9 > 4.> 2 < 10 >7 < 8 8, 1 9
        '''
        l = 0
        r = 1
        sign = ""
        ans = 1
        
        while r < len(arr):
            if arr[r-1] > arr[r]   and sign != ">":
                    ans = max(ans,r-l+1)
                    r += 1
                    sign = ">"
            elif  arr[r-1] < arr[r] and sign != "<":
                    ans = max(ans,r-l+1)
                    r += 1
                    sign = "<"

            else:
                 r = r + 1 if arr[r] == arr[r-1] else r
                 l = r - 1
                 sign = ""
        
        
        return ans