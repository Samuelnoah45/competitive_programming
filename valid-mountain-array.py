class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]<arr[i+1]:
                i += 1
            
            elif arr[j]<arr[j-1]:
                j -= 1
            
            else:
                break
            
        
        return i!=0 and j!=len(arr) -1  and arr[i]==arr[j]