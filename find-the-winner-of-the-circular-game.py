class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    
        nums=[i+1 for i in  range(n)]
        def iterative(i):
            
            while len(nums) > 1:
                nums.pop((i))
                i = (i + k - 1) % len(nums)
            return nums[0]

        def recur(i):
            #base case
            if len(nums) <= 1:
                return

            #recurence relation
            nums.pop(i)
            recur((i + k - 1) % len(nums))
            
        recur(k-1)

        return nums[0]