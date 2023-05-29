class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxIdx = n
        val = float('inf')
        for i in range(n)[::-1]:
            if arr[i] <= val:
                val = arr[i]
            else:
                maxIdx = i
                maxVal = 0
                for j in range(i+1, n):
                    if arr[j] < arr[i]:
                        if maxVal < arr[j]:
                            maxVal = arr[j]
                            maxIdx = j
                else:
                    arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
                return arr

        return arr