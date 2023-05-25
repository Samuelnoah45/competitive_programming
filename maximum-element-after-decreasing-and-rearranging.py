class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr = sorted(arr)
        arr[0] = 1   

        for i in range(len(arr) - 1):
            if 0 <= abs(arr[i] - arr[i+1]) <= 1:
                continue
            arr[i+1] = arr[i] + 1

        return max(arr)