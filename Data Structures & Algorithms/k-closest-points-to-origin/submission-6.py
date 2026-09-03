class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if k == len(points):
            return points

        def distance(x, y):
            return math.sqrt(x**2 + y**2)

        def quick_select(l, r):

            pivot, p = distance(points[r][0], points[r][1]), l

            for i in range(l, r):

                x, y = points[i]
                if distance(x, y) <= pivot:
                    points[i], points[p] = points[p], points[i]
                    p += 1

            points[p], points[r] = points[r], points[p]

            if p < k:
                return quick_select(p + 1, r)
            elif p > k:
                return quick_select(l, p - 1)
            else:
                return points[:p]

        return quick_select(0, len(points)-1)
