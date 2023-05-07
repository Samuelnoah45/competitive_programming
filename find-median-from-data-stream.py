class MedianFinder:

    def __init__(self):
        self.H1 = []
        self.H2 = []

    def addNum(self, num: int) -> None:
        heappush(self.H1, -num)

        if len(self.H1) - len(self.H2) > 1:
            heappush(self.H2, -heappop(self.H1))
        
        if self.H1 and self.H2 and -self.H1[0] > self.H2[0]:
            tt = heappop(self.H1)
            tmp = heapreplace(self.H2, -tt)
            heappush(self.H1, -tmp)

    def findMedian(self) -> float:
        if len(self.H1) == len(self.H2):
            return (-self.H1[0] + self.H2[0]) / 2
        elif len(self.H1) > len(self.H2):
            return -self.H1[0]
        else:
            return self.H2[0]


    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()