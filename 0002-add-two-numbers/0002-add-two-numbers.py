# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        rem = 0
        while l1 != None or l2 != None:
            if l1 and l2:
                sumV= l1.val+l2.val+rem
                ans.next = ListNode(sumV%10)
                ans = ans.next
                rem = sumV//10
                l1 = l1.next
                l2 = l2.next

            elif l1:
                sumV= l1.val+rem
                ans.next = ListNode(sumV%10)
                ans = ans.next
                rem = sumV//10
                l1 = l1.next
            elif l2:
                sumV= l2.val+rem
                ans.next = ListNode(sumV%10)
                ans = ans.next
                rem = sumV//10
                l2 = l2.next
                
        if rem != 0:
          ans.next = ListNode(rem)

        return head.next





        





