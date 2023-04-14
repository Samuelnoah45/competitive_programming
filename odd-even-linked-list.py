# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if not head.next.next:
            return head
        pre = head
        cur = head.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = cur.next
            tmp.next = pre.next
            pre.next = tmp
            pre = pre.next
        return head