class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = 1, max(piles)
        min_k = float('inf')
        while l <= r:

            mid = l + ((r - l) // 2)
            
            work = 0
            for num in piles:
                work += math.ceil(num / mid)
            print(f"work at {mid} = {work}")
            if work <= h:
                min_k = mid
                r = mid - 1
            else:
                l = mid + 1

        
        return min_k