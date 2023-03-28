# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head 
        count = 0
        ans = 0
        while curr != None:
            curr = curr.next
            count += 1
        half = count//2
        count = 0 
        curr = head
        prev = None
        while curr != None:
            count += 1
            if count == half:
                prev = curr
                curr = curr.next
            elif count > half:
                next = curr.next 
                curr.next = prev 
                prev = curr
                curr = next
            else:
                curr = curr.next
        left = head
        for i in range(half):
            ans = max(prev.val+left.val,ans)
            prev = prev.next
            left = left.next


        return ans