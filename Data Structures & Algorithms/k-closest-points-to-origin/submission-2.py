class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        distances = [([x, y], distance(x, y)) for x, y in points]
        target_idx = len(points) - k

        def quick_select(l, r):
            pivot, p = distances[r][1], l

            for i in range(l, r):
                if distances[i][1] > pivot:
                    distances[i], distances[p] = distances[p], distances[i]
                    p += 1

            distances[p], distances[r] = distances[r], distances[p]

            if p < target_idx:
                return quick_select(p + 1, r)
            elif p > target_idx:
                return quick_select(l, p - 1)
            else:
                return distances[p:]

        ret = quick_select(0, len(points)-1)
        return [points for points, _ in ret ]

