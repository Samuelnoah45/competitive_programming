class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num1Hash = {}
        for num in nums1:
            num1Hash[num] = -1
        stack = []

        for num in nums2:
            if stack:
                while stack and stack[-1] < num:
                    if stack[-1] in num1Hash:
                        num1Hash[stack[-1]] = num
                    stack.pop()
                stack.append(num)


            else:
                stack.append(num)

        return list(num1Hash.values())