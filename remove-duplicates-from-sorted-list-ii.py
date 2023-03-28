# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

1
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.val
                while cur and cur.val == temp:
                    cur = cur.next
                if prev:
                    prev.next = cur
                else:
                    head = cur
            else:
                prev, cur = cur, cur.next
        return head
'''
cur = 1 check 2 cur = 2, prev = 1
cur = 2 check 3 cur = 3, prev = 2
cur = 3 check 3 cur = 4, prev.next = cur

'''