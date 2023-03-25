class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l = 0
        r = len(arr) -1
        peak = 0
        while l <= r:
            md = l + (r - l)//2
            
            if arr[md - 1] < arr[md] > arr[md + 1]:
                peak = md 
                break
            if arr[md - 1] > arr[md]:
                r = md 
            else:
                l = md 

        return peak