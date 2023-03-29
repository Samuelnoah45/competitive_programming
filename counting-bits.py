class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            bit = num
            count = 0
            while bit:
                if bit % 2!=0:
                    count += 1
                bit = bit>>1

            ans.append(count)
        return ans