class Solution: 
    def select(self, arr, i):
        min_ = arr[i]
        min_idx = i
        n = len(arr)
        while i < n:
            if arr[i] < min_:
                min_ = arr[i]
                min_idx = i
            i += 1
        return min_idx
    
    def selectionSort(self, arr,n):
        for i in range(n):
            selected = self.select(arr, i)
            arr[i], arr[selected] = arr[selected], arr[i]