class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        ans, curr = 0, []
        used = 0

        def build(i=0):
            nonlocal used, ans
            if curr and (curr[-1] % len(curr) != 0) and (len(curr) % curr[-1] != 0):
                return 

            if i == len(nums):
                ans += 1
                return

            for idx, num in enumerate(nums):
                if  (used & (1 << idx)) == 0:
                    used |= 1 << idx
                    curr.append(num)
                    build(i+1)
                    curr.pop()
                    used ^= 1 << idx
        build()
        return ans