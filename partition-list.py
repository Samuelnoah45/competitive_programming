# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
       
        leftNode = ListNode()
        leftHead= leftNode
        rightNode = ListNode()
        rightHead= rightNode
        curr = head 

        while curr:
            if curr.val >= x:
                rightNode.next = curr
                rightNode = rightNode.next 
            else:
                leftNode.next = curr
                leftNode =leftNode.next
            curr = curr.next
        
     

        rightNode.next = None
        leftNode.next =  rightHead.next
     
        return leftHead.next