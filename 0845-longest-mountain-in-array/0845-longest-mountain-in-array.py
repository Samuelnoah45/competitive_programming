class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        if len(arr) < 3:
            return 0
        i = 1
        counter = 0
        ans =0
        while i < len(arr) -1:
            if arr[i-1] < arr[i] > arr[i+1]:
                left = i-1
                right = i+1
                while left > 0 and  arr[left-1] < arr[left]:
                    left -=1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right +=1
                ans = max(right-left+1,ans)
                
                i = right
            i += 1


        return ans


        
