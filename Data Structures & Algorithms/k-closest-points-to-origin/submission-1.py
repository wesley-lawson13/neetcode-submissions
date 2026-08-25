class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        # first, calculate all distances O(n)
        max_heap = []
        for x, y in points:
            dist = -distance(x, y)
            heapq.heappush(max_heap, [dist, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [[x, y] for _, x, y in max_heap]

