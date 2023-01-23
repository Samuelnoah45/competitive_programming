class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0 
        r = k
        ans = sum(arr[l:r])
        count = 0
        
        while r < len(arr):
            if ans/k >= threshold:
                count += 1
            ans += (arr[r]-arr[l])
            r += 1
            l += 1
        
        if ans/k >=threshold:
            count+=1
            

        return count

        