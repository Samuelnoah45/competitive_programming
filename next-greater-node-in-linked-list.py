# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        Hash = {}
        node = head
        nums = []

        while node:
            nums.append(node.val)
            node = node.next
        for idx in range(len(nums)):
            Hash[idx] = 0
        print(nums)
        stack = []
        for idx , num in enumerate(nums):
            if stack:
                while stack and nums[stack[-1]] < num:
                    Hash[stack[-1]] = num
                    poped = stack.pop()

                stack.append(idx)

            else:
                stack.append(idx)

        return list(Hash.values())