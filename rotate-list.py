# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        tail = node

        offset = abs(k) % length
        if offset == 0:
            return head

        new_tail_position = length - offset if k > 0 else offset
            
        counter = 1
        node = head
        while node.next:
            if counter ==new_tail_position:
                final_tail = node
                break
            node = node.next
            counter += 1

        tail.next = head
        head = final_tail.next
        final_tail.next = None

        return head