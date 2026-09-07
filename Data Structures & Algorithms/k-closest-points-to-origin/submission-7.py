class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        if len(points) == k:
            return points

        target_idx = k
        def quick_select(l, r):
            pivot, p = dist(points[r][0], points[r][1]), l

            for i in range(l, r):
                if dist(points[i][0], points[i][1]) < pivot:
                    points[i], points[p] = points[p], points[i]
                    p += 1

            points[r], points[p] = points[p], points[r]
            print(points)

            if p > target_idx:
                return quick_select(l, p - 1)
            elif p < target_idx:
                return quick_select(p + 1, r)
            else:
                return points[:p]

        return quick_select(0, len(points)-1)

