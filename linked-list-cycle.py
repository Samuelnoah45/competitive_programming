# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        
        move       = lambda n: n.next if n else None
        
        fast, slow = head, head
        
        while fast:
            fast = move(move(fast))
            slow =      move(slow)
            
            if fast and fast == slow:
                return True
        
        return False