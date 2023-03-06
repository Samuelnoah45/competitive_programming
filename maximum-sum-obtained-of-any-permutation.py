class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        arr = [0] *( len(nums) + 1)

        for start , end in requests:
            arr[start] += 1
            arr[end + 1]  -= 1

        arr.pop()
        arr = list(accumulate(arr))

        arr.sort()
        nums.sort()

        sum_ = 0
        for i in range(len(arr)):
            sum_ += (arr[i]*nums[i])


        return sum_ % (pow(10,9) + 7)