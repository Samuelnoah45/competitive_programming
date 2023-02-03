class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.dummy = Node(None)

    def get(self, index: int) -> int:
        count = 0
        cur = self.dummy.next
        while cur and count<index:
            count+=1
            cur = cur.next
        if not cur:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        count = 0
        cur = self.dummy

        while cur.next and count<index:
            cur = cur.next
            count+=1

        if count == index:
            new_node.next = cur.next
            cur.next = new_node  

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        cur = self.dummy

        while cur.next and count<index:
            cur = cur.next
            count+=1
        
        if cur.next:
            cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)