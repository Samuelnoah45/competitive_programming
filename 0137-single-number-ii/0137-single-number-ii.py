class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits  = defaultdict(int)
        negativecount = 0
        for num in nums:
            if num < 0:
                negativecount += 1
            num = abs(num)
        
            count = 0
            while num != 0 and count<32:
                if num & 1 != 0:
                    bits[count] += 1
                num>>=1
                count+=1
        ans = 0
        for i in bits:
            if bits[i]%3!=0:
                mask = 1 << i
                ans |= mask
        if negativecount %3 == 1:
            ans = -ans
        return ans

        