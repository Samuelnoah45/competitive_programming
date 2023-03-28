class Solution(object):
    def replaceElements(self, arr):
	
        max_right = arr[-1]
        current = 0
        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
                max_right = current
                      
        arr[len(arr)-1] = -1
        return arr