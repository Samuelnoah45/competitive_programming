class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key = lambda x : x[2] )
        arr = [0] * (trips[-1][2] + 1)

        for num , start ,end in trips:
                arr[start] +=  num
                arr[end] -= num


        arr.pop()

        arr = list(accumulate(arr))

        return max(arr) <= capacity