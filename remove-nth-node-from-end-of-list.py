# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Head = head
        counter = 0
        while Head != None:
            Head = Head.next
            counter += 1
        n = counter -n
        if n == 0:
            head = head.next
            return head
        Head = head
        for i in range(n-1):
            Head = Head.next
        if Head.next != None:
            Head.next = Head.next.next
        else:
            Head.next = None

        return head