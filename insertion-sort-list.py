# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        1,2,3,1,2,5,6
        '''
        dummy = ListNode(0)
        dummy.next = head 
        curr= head

        while curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                pre = dummy 

                while pre.next.val <= curr.next.val:
                    pre = pre.next
                temp = curr.next
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp 

        return dummy.next