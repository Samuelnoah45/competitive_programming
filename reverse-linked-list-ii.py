# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next=  head 
        head1 = dummy

        for i in range(left-1):
            head1 = head1.next 

        p = head1.next 

        for j in range(right-left):
            temp = head1.next 
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = temp 
            
        return dummy.next