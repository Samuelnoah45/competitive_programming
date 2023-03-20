class MyCircularDeque:

    def __init__(self, k: int):
            self.k = k
            self.arr = []
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.arr = [value] + self.arr
            return True
        else:
            return False
    
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.arr = self.arr + [value]
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.arr = self.arr[1:]
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.arr = self.arr[:-1]
            return True
        else:
            return False        
    def getFront(self) -> int:
        if not self.isEmpty():
            return self.arr[0]
        else:
            return -1 
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1 
    def isEmpty(self) -> bool:
        return len(self.arr) == 0
        
    def isFull(self) -> bool:

        return len(self.arr) >= self.k

        
        


# # Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()