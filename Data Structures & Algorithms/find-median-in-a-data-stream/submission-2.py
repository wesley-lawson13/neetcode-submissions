class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:

        if self.right and num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.right) > len(self.left) + 1:
            pop = heapq.heappop(self.right)
            heapq.heappush(self.left, -pop)
        elif len(self.left) > len(self.right) + 1:
            pop = heapq.heappop(self.left)
            heapq.heappush(self.right, -pop)
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        if len(self.right) > len(self.left):
            return self.right[0]

        return (-self.left[0] + self.right[0]) / 2
        
        