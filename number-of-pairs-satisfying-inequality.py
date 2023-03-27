class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.diff = diff
        self.count = 0
        sub = [x[0] - x[1] for x in zip(nums1 , nums2)]
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m
        
            # create temp arrays
            L = [0] * (n1)
            R = [0] * (n2)
            # Copy data to temp arrays L[] and R[]
            for i in range(0, n1):
                L[i] = arr[l + i]
        
            for j in range(0, n2):
                R[j] = arr[m + 1 + j]
            idx1 = 0
            idx2 = 0
            while idx1 < len(L) and idx2 < len(R):
                if L[idx1] - self.diff <= R[idx2]:
                    self.count += len(R) - idx2
                    print(len(R) - idx2)
                    idx1 += 1
                else:
                    idx2 += 1

            
        
            # Merge the temp arrays back into arr[l..r]
            i = 0     # Initial index of first subarray
            j = 0     # Initial index of second subarray
            k = l     # Initial index of merged subarray

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
        
            # Copy the remaining elements of L[], if there
            # are any
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
        
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

            
        def mergeSort(sub, l, r):
                if l < r:
                # Same as (l+r)//2, but avoids overflow for
                # large l and h
                    m = l+(r-l)//2
            
                    # Sort first and second halves
                    mergeSort(sub, l, m)
                    mergeSort(sub, m+1, r)
                    merge(sub, l, m, r)
        mergeSort(sub ,0 , len(sub) -1)
        print(sub)
        return self.count