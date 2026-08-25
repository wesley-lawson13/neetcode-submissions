class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        # first, calculate all distances O(n)
        heap = []
        for x, y in points:
            dist = distance(x, y) * -1 #invert for max heap
            heap.append([dist, x, y])
        
        # set up max heap on dist
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        ret = []
        for _, x, y in heap:
            ret.append([x, y])

        return ret

