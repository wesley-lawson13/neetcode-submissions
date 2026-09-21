class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        if k == len(points):
            return points
        
        def quick_select(l, r):
            pivot, p = dist(points[r][0], points[r][1]), l

            for i in range(l, r):

                if dist(points[i][0], points[i][1]) < pivot:
                    points[p], points[i] = points[i], points[p]
                    p += 1

            points[p], points[r] = points[r], points[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return points[:p]

        return quick_select(0, len(points) - 1)