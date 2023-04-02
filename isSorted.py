#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        l = 0
        r = 1
        while r < n:
            
            if arr[l] > arr[r]:
                
                return False
                
            r += 1
            l += 1
        return True