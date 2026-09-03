class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        heap = []
        for x, y in points:
            dist = distance(x, y)
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]