class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        bits = defaultdict(int)

        while num != 0:
            if num & 1 == 0:
                bits[count] = 1
            num >>=1
            count += 1
        
        ans = 0
        for i in bits:
            if bits[i] == 1:
                mask = 1 << i
                ans |= mask
        return ans