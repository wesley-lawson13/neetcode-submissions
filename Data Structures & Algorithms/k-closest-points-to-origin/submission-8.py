class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        heap = [] # heap of size k

        for x, y in points:
            distance = dist(x, y)
            heapq.heappush(heap, [-distance, x, y])

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]